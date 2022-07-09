from django.urls import path, include
from . import views

urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete_task'),
    path('complete/<int:id>/', views.complete, name='completed_task'),
    path('', views.tasks, name='tasks'),
]
