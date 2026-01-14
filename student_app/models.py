from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=60)
    age = models.IntegerField()
    roll_number = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.full_name