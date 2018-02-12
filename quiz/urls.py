from django.conf.urls import url
from django.contrib.auth import views as auth_views
from quiz import views

app_name = 'quiz'

urlpatterns = [
    url(r'^question/$', views.question, name='question'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create_a_quiz_view, name='create_a_quiz_view')
]