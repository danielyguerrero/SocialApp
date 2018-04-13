from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.index, name="dashboard"),

    url(r'^addfriend/(?P<friendid>[0-9]+)$', views.add_friend, name="add_friend"),

    url(r'^remfriend/(?P<friendid>[0-9]+)$', views.remove_friend, name="remove_friend"),
    
    url(r'^showuser/(?P<userid>[0-9]+)$', views.show_user, name="show_user"),

]


