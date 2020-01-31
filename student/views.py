from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm

def index(request):
    students = Student.objects.all()
    return render(request, 'student/index.html', context = {'students': students})

def info(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("没找到该学员")
    return render(request, 'student/info.html', {'student': student})

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valide():
            form.save()
            return HttpReponseRedirect(reverse('student/index'))
    else:
        form = StudentForm()

    return render(request, 'student/register.html', context = {'form': form})