from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

# Create your views here.
from quiz.models import Question, Answer, Exam
from django.core.mail import send_mail
from . import forms

def question(request):
	question_list = Question.objects.order_by('-pub_date')[:5]
	return render(request, 'quiz/question.html', {'question_list': question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})

def create_a_quiz_view(request):
	form = forms.Create_a_quiz_Form()
	return render(request, 'quiz/form.html', {'form': form})