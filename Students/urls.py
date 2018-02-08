from django.conf.urls import url

from Students import views

app_name = 'Students'

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),

    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),

]