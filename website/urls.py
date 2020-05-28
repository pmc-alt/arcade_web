from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('requests', views.request, name="request"),
]
