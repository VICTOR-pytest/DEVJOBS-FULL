from django import forms
from .models import Job
from companies.models import Company

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'title', 'description', 'salary_range', 'level', 'is_active']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        # Só empresas do usuário aparecem no select
        self.fields['company'].queryset = Company.objects.filter(owner=user)
