from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('my_jobs/', views.my_jobs, name='my_jobs'),
    path('new/', views.job_create, name='job_create'),
    path('<int:pk>/edit/', views.job_update, name='job_update'),
    path('<int:pk>/delete/', views.job_delete, name='job_delete'),
]
