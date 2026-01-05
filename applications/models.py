from django.db import models

from django.contrib.auth.models import User
from jobs.models import Job

class Application(models.Model):
    """
    Candidatura de um usuário a uma vaga.
    """

    STATUS_CHOICES = (
        ('AP', 'Applied'),
        ('RV', 'Reviewing'),
        ('AC', 'Accepted'),
        ('RJ', 'Rejected'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='AP'
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return f'{self.user.username} -> {self.job.title}'

