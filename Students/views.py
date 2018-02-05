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

    p = {'x' : "welcome at quiz app!"}

    return render(request, "Students/index.html", context = p)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/question_detail.html', {'question': question})
