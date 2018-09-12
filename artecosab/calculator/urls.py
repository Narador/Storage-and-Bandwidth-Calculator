''' calculator urls '''

from django.urls import re_path
from . import views

app_name = 'calculator'

urlpatterns = [
    # Index
    re_path('^$', views.IndexView.as_view(), name='index'),
    # Server
    re_path('^(?P<pk>[0-9]+)/$', views.ServerView.as_view(), name="server")
]
