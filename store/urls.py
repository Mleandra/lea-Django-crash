from django.conf.urls import url
from django.urls import path
from . import views

app_name='store'
urlpatterns=[
   url(r'^$',views.index, name='index'),
   url(r'^liste/$',views.listage, name='listage'),
   url(r'^(?P<manga_id>[0-9]+)/$', views.detail, name='detail'),
   url(r'^recherche/$', views.recherche, name='recherche'),
]