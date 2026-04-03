from django.db import models
from student.models import Student   # adapt if needed
from teacher.models import Teacher # adapt if needed
from departement.models import Departement
from subject.models import Subject


class Exam(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_Finished = models.BooleanField(default=False)
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
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="results")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")

    mark = models.FloatField()
    status = models.CharField(
        max_length=10,
        choices=[('PASS', 'Pass'), ('FAIL', 'Fail')]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('exam', 'student')  # 🔥 VERY IMPORTANT

    def __str__(self):
        return f"{self.student} - {self.exam} ({self.mark})"