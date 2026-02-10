from django.db import models

# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return self.courseName

  