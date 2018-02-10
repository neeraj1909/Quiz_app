from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from . import forms

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from Students.models import Question


def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)


def index(request):
    '''context = {
        "questions": Question.objects.all()
    }'''

    return render(request, "Students/index.html")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/question_detail.html', {'question': question})


class register(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("Students:login")
    template_name = "Students/registration.html"


    # # All code for registration here.
    # return render(request, "Students/registration.html")


# def login(request):


#   # Add code here for login 

#   return render(request, "Students/login.html")

def question(request):
    return render(request, 'Students/question.html') 