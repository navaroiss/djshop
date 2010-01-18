from django.conf import settings

def setting_global(request):
    return {
        'items_in_bag':1,
        'media_url':settings.MEDIA_URL
    }