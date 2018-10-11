from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^display/$', views.handleform, name='handleform'),
]