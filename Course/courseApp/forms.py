from django.db import models
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['courseName', 'description', 'instructor', 'credits']

