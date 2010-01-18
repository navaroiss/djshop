from django.utils.cache import patch_vary_headers
from django.utils import translation
from django.conf import settings

import re, logging

class LocaleURLMiddleware:
    def get_language_from_request (self,request):
        global response
        supported = dict(settings.LANGUAGES)
        lang = request.GET.get('language')
        if lang in supported:
            if hasattr(request, 'session'):
                request.session['django_language'] = lang
            else:
                response.set_cookie('django_language', lang)
        if hasattr(request, 'session'):
            lang = request.session.get('django_language', None)
            if lang in supported and lang is not None:
                return lang
        else:
            lang = request.COOKIES.get('django_language', None)
            if lang in supported and lang is not None:
                return lang
        
    def process_request(self, request):
        language = self.get_language_from_request(request)
        if language is None:
            language = settings.LANGUAGE_CODE
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()
        
    def process_response(self, request, response):
        patch_vary_headers(response, ('Accept-Language',))
        translation.deactivate()
        return response
