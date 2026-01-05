from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobForm
from .models import Job


@login_required
def my_jobs(request):
    """
    Lista apenas as vagas criadas pelo usuário logado.
    Isso é essencial para controle de acesso e UX.
    """
    jobs = Job.objects.filter(company__owner=request.user)

    return render(request, "jobs/my_jobs.html", {"jobs": jobs})

@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(user=request.user)

    return render(request, 'jobs/job_form.html', {'form': form})



@login_required
def job_list(request):
    jobs = Job.objects.filter(company__owner=request.user)
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk, company__owner=request.user)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job, user=request.user)

    return render(request, 'jobs/job_form.html', {'form': form})

@login_required
def job_delete(request, pk):
    job = get_object_or_404(
        Job,
        pk=pk,
        company__owner=request.user
    )

    if request.method == 'POST':
        job.delete()
        return redirect('job_list')

    return render(request, 'jobs/job_confirm_delete.html', {'job': job})



