from django.shortcuts import redirect, render
from .models import Course
from .forms import CourseForm   

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courseApp/course_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courseApp/course_form.html', {'form': form})

def course_update(request, pk): 
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courseApp/course_form.html', {'form': form})

def course_delete(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'courseApp/course_confirm_delete.html', {'course': course})