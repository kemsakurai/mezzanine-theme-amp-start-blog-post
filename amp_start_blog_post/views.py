from django.views import View
from django.http import HttpResponse
from django.http import Http404
import urllib.parse
from pathlib import Path

class OptimizedAmpView(View):
    def get(self, request, *args, **kwargs):
        base_url =  urllib.parse.quote(request.path)
        elems = base_url.split("/")
        file_name = elems[len(elems) -2][:100] + ".html"
        response = HttpResponse(content_type="text/html")
        directory = str(Path(__file__).resolve().parents[1])
        try:
            for line in open(directory + '/amp_start_blog_post/templates/amp_start_blog_post/htmls/' + file_name):
                response.write(line)
        except FileNotFoundError:
            raise Http404("Page does not exist")
        return response            