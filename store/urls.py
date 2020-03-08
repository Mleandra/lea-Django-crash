from django.conf.urls import url
from django.urls import path
from . import views

app_name='store'
urlpatterns=[
   url(r'^$',views.index ,name='accueil'),
   url(r'^(?P<manga_id>[0-9]+)/$', views.detail, name='detail'),
  # url(r'^search/$', views.search, name='search'),
]