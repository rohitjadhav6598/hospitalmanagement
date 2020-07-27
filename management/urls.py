from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='management-home'),
    path('list/', views.list, name='management-list'),
]
