from django.contrib import admin
from django.urls import path , include 
from django.shortcuts import redirect
from users.views import RegisterView


def home(request):
    return redirect('job_list')


urlpatterns = [
    path('', home, name='home'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('applications/', include('applications.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('jobs/', include('jobs.urls')),
    path('companies/', include('companies.urls')),
    path('admin/', admin.site.urls),
]