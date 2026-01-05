from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect
from django.db import IntegrityError

from applications.forms import ApplicationStatusForm
from jobs.models import Job
from .models import Application

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, is_active=True)

    try:
        Application.objects.create(
            user=request.user,
            job=job
        )
    except IntegrityError:
        # já se candidatou
        pass

    return redirect('job_public_list')


@login_required
def my_applications(request):
    applications = request.user.applications.select_related('job', 'job__company')
    return render(request, 'applications/my_applications.html', {
        'applications': applications
    })

@login_required
def received_applications(request):
    applications = Application.objects.filter(
        job__company__owner=request.user
    ).select_related('user', 'job')

    return render(request, 'applications/received_applications.html', {
        'applications': applications
    })
@login_required
def update_application_status(request, pk):
    application = get_object_or_404(
        Application,
        pk=pk,
        job__company__owner=request.user
    )

    if request.method == 'POST':
        form = ApplicationStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('received_applications')
    else:
        form = ApplicationStatusForm(instance=application)

    return render(request, 'applications/application_status_form.html', {
        'form': form,
        'application': application
    })

