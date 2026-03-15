from django.db import models

class Course(models.Model):
    courseName = models.CharField(max_length=100, default="Unknown Course")
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return self.courseName

