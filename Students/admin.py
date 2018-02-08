from django.contrib import admin

# Register your models here.
from .models import Question, Student, Choice

admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Choice)