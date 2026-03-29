from django.db import models

# Create your models here.

class Departement(models.Model):
    name = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.code})"
