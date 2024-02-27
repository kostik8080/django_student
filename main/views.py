from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from main.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'main/index.html'
    context_object_name = 'objects_list'
    extra_context = {'title': 'Главная'}

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        print(f"{name} ({email}): {massage}")

    context = {
        'title': 'Контакт'
    }

    return render(request, 'main/contact.html', context)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student_detail.html'
    context_object_name = 'object_list'
    extra_context = {'title': 'Студент'}


def view_student(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    context = {
        'object_list': student_item
    }
    return render(request, 'main/student_detail.html', context)
