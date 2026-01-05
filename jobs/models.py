from django.db import models

from companies.models import Company

class Job(models.Model):
    """
    Vaga publicada por uma empresa.
    """

    LEVEL_CHOICES = (
        ('JR', 'Júnior'),
        ('PL', 'Pleno'),
        ('SR', 'Sênior'),
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    salary_range = models.CharField(max_length=50)
    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.company.name}'
