from django.db import models
from student.models import Student   # adapt if needed
from teacher.models import Teacher # adapt if needed
from departement.models import Departement


class Exam(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    departement = models.ForeignKey(
        Departement,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.name} - {self.subject}"


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.FloatField()
    status = models.CharField(
        max_length=10,
        choices=[('PASS', 'Pass'), ('FAIL', 'Fail')]
    )

    def __str__(self):
        return f"{self.student} - {self.exam}"