from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:pk>', views.read_more, name='read_more'),
]