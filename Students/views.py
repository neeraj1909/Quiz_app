from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import request, HttpResponse
from django.template import RequestContext
#from django.urls import reverse

from Students.models import Student, Question, Choice

# Create your views here.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'Students/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def index(request):
    context = RequestContext(request)
    return render_to_response( "quiz/index.html", {}, context_instance = context)


