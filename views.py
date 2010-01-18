from django.shortcuts import render_to_response
from django.utils.cache import patch_vary_headers
from django.utils import translation
from django.template.context import RequestContext

def home_page(request):
    return render_to_response('home.html', RequestContext(request))