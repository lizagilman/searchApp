from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_extensions.routers import ExtendedDefaultRouter

from app.views import IndexView


router = ExtendedDefaultRouter()



admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', IndexView.as_view(), name='index'),
    url(r'apis/', include(router.urls)),
]
