from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('object_recognition', views.object_recognition, name='object_recognition'),
]