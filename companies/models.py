from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    """
    Representa uma empresa que pode publicar vagas.
    Um usuário pode ser dono de uma ou mais empresas.
    """

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='companies'
    )
    name = models.CharField(max_length=150)
    description = models.TextField()
    website = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

