from django.db import models

# Create your models here.

class Student(models.Model):
  student_id = models.CharField(max_length = 20,primary_key = True)
  student_password = models.CharField(max_length = 20)

  def display(self):
     return f"{self.student_id} {self.student_password}"

  def _str_(self):
     return self.display()