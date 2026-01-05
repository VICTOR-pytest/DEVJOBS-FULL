from django.shortcuts import render

# users/views.py
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class RegisterView(CreateView):
    model = User
    fields = ['username', 'password']
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Salvar a senha criptografada
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)
