from django.urls import re_path
from django.conf.urls import include
from django.conf import settings

from .views import index

urlpatterns = [
    # re_path(r'^$', LoginView.as_view(), name='login'),
    re_path(r'', index, name='index')
]
