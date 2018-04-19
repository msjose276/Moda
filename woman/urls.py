

from django.urls import path

from . import views

urlpatterns = [
    path('', views.woman, name='woman'),
]