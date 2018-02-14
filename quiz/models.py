# Create your models here.

from django.db import models
from django.contrib import auth
from django.utils import timezone

class Answer(models.Model):
    """
    Answer's Model, which is used as the answer in Question Model
    """
    text = models.CharField(max_length=128, verbose_name=u'Answer\'s text')
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Question(models.Model):
    question_text = models.CharField(max_length=256, verbose_name=u'Question\'s text')
    answers = models.ManyToManyField(Answer)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{content} - {published}".format(content=self.question_text, published=self.is_published)

class Exam(models.Model):
    """
    Exam's model, works as a wrapper for the questions
    """
    name = models.CharField(max_length=64, verbose_name=u'Exam name', )
    slug = models.SlugField()
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


#model for creating a quiz
# class Create_a_Quiz(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length = 200)
#     created_date = models.DateTimeField(default = timezone.now)
#     published_date = models.DateTimeField(blank = True, null = True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title
    