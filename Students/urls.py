from django.conf.urls import url
from django.contrib.auth import views as auth_views
from Students import views

app_name = 'Students'

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^register$', views.register.as_view(), name='register'),
    # url(r'^login$', views.login, name='login'),
    url(r"login/$", auth_views.LoginView.as_view(template_name="Students/login.html"),name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),

    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),

]