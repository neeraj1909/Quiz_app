from django.contrib import admin

# Register your models here.
from .models import Answer, Question, Exam

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Exam)