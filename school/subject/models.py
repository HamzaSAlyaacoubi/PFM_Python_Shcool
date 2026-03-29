from django.db import models
from departement.models import Departement

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    
    departement = models.ForeignKey(
        Departement,
        on_delete=models.CASCADE,
        related_name='subjects',
    )
    
    def __str__(self):
        return f"{self.name} ({self.code})"
