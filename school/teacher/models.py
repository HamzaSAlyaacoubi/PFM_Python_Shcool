from django.db import models
from departement.models import Departement

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    gender = models.CharField(max_length=10, choices=[('Male','Male'), ('Female','Female')]) 
    date_of_birth = models.DateField() 
    joining_date = models.DateField() 
    mobile_number = models.CharField(max_length=15) 
    teacher_image = models.ImageField(upload_to='teachers/', blank=True) 

    departement = models.ForeignKey(
        Departement,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='teachers'
    )
    
    def __srt__(self):
        return f"{self.first_name} {self.last_name}"
