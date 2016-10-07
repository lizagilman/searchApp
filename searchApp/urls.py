from django.conf.urls import include, url
from app import urls


urlpatterns = [
    url(r'^searchApp/', include(urls)),
]