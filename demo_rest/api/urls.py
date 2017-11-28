# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_modules

urlpatterns = {
    url(r'^modules/$', get_modules, name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)