from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('my/', views.my_applications, name='my_applications'),
    path('received/', views.received_applications, name='received_applications'),
    path('<int:pk>/status/', views.update_application_status, name='application_status'),
]
