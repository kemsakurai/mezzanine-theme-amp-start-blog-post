from django.views import View
from django.shortcuts import render
from django.conf import settings as django_settings
import urllib.parse    

class OptimizedAmpView(View):
    def get(self, request, *args, **kwargs):
        base_url =  urllib.parse.quote(request.path)
        elems = base_url.split("/")
        
        file_name = elems[len(elems) -2][:100] + ".html"
        return render(request, 'amp_start_blog_post/htmls/' + file_name)
