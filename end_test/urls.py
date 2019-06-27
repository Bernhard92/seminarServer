from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('start_test', views.start_test, name='start_test'),
    path('check_test', views.check_test, name='check_test'),
]