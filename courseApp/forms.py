from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['courseName', 'description', 'instructor', 'credits']
        widgets = {
            'courseName': forms.TextInput(attrs={'class': 'form-control'}),     

            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'instructor': forms.TextInput(attrs={'class': 'form-control'}), 
            'credits': forms.NumberInput(attrs={'class': 'form-control'}),
        }