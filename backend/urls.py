from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from api.views import ProductView, SlidersView, ConfigsView
from rest_framework import routers

from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

from django.views.static import serve

router = routers.DefaultRouter()
router.register("products", ProductView)
router.register("sliders", SlidersView)
router.register("configs", ConfigsView)

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/accounts/', include('accounts.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    
    


    # Add a URL pattern for serving media files during development
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT))

