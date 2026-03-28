from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    teacher_id = models.CharField(max_length=20) 
    gender = models.CharField(max_length=10, choices=[('Male','Male'), ('Female','Female')]) 
    date_of_birth = models.DateField() 
    joining_date = models.DateField() 
    mobile_number = models.CharField(max_length=15) 
    teacher_image = models.ImageField(upload_to='teachers/', blank=True) 
    
    def __self__(self):
        return f"{self.first_name} {self.last_name}"
