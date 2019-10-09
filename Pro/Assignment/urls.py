from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^home$',views.home,name='home'),
    url(r'^all$',views.view12,name='view12'),
    url(r'^save$',views.store,name='saved'),
    url(r'^(?P<id>\d+)/edit$',views.edit,name='edit'),
    url(r'^(?P<id>\d+)/update$',views.updateNote,name='update'),
    url(r'^(?P<id>\d+)/deleted$',views.deleted,name='deleted'),
    url(r'^$',views.front,name='front'),


]
