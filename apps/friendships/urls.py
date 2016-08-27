from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^friends$', views.friends, name="friends"),
    url(r'^user/(?P<id>\d+)$$', views.show_user, name="show_user"),
    url(r'^delete_friend/(?P<id>\d+)$', views.delete_friend, name="delete_friend"),
    url(r'^add_friend$', views.add_friend, name="add_friend"),
]

# /(?P<id>\d+)$