from __future__ import unicode_literals

from django.template import Template

from mezzanine.utils.device import templates_for_device
from mezzanine.utils.deprecation import (MiddlewareMixin)


class TemplateForAMPMiddleware(MiddlewareMixin):
    """
    Inserts device-specific templates to the template list.
    """
    def process_template_response(self, request, response):

        url = request.get_full_path()
        if url.startswith("/blog/amp/"):
        # If a device wasn't set via cookie, match user agent.
            try:
                request.META["HTTP_USER_AGENT"] = "amp"
            except KeyError:
                pass
            # if hasattr(response, "template_name"):
            #     if not isinstance(response.template_name, Template):
            #         templates = response.template_name
            #         if not isinstance(templates, (list, tuple)):
            #             templates = [templates]
            #         device_templates = []
            #         for template in templates:
            #             device_templates.append("%s/%s" % ("amp_start_blog_post", template))
            #         response.template_name = device_templates
        if hasattr(response, "template_name"):
            if not isinstance(response.template_name, Template):
                templates = templates_for_device(request, response.template_name)
                response.template_name = templates
        return response
