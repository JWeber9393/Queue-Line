from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^nq_user(?P<user_id>\d+)$', views.nq_user),
    url(r'^dq_user(?P<user_id>\d+)$', views.dq_user),
    url(r'^queue_list$', views.queue_list),
    url(r'^create_user$', views.create_user),
    url(r'^$', views.index),
]
