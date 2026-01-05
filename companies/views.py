from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CompanyForm

@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user  # regra de negócio
            company.save()
            return redirect('company_list')
    else:
        form = CompanyForm()

    return render(request, 'companies/company_form.html', {'form': form})

@login_required
def company_list(request):
    companies = request.user.companies.all()
    return render(request, 'companies/company_list.html', {
        'companies': companies
    })

from django.shortcuts import get_object_or_404

@login_required
def company_update(request, pk):
    company = get_object_or_404(
        company,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)

    return render(request, 'companies/company_form.html', {
        'form': form
    })


@login_required
def company_delete(request, pk):
    company = get_object_or_404( company, pk=pk,owner=request.user)

    if request.method == 'POST':
        company.delete()
        return redirect('company_list')

    return render(request, 'companies/company_confirm_delete.html', {
        'company': company
    })
