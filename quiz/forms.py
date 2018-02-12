from django.core import validators
from django import forms

class Create_a_quiz_Form(forms.Form):
	topic = forms.CharField(required=True, max_length = 30)
	about_the_quiz = forms.CharField(widget=forms.Textarea)
	creator = forms.EmailField()