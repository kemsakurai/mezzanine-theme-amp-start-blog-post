from amp_start_blog_post import set_amp_detect

class AMPDetectionMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(self, request):
        if '/amp/' in request.path:
            set_amp_detect(is_amp_detect=True, request=request)
        else:
            set_amp_detect(is_amp_detect=False, request=request)
