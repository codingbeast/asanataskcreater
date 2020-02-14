from django.conf.urls import url
from TaskCreater import views

app_name = 'TaskCreater'
urlpatterns = [
  # The home view ('/tutorial/')
  url(r'^$', views.home, name='index'),
  # Explicit home ('/tutorial/home/')
  url(r'^home/$', views.home, name='home'),
  # Redirect to get token ('/tutorial/gettoken/')
  url(r'^view/$', views.view, name='view'),
  url(r'^gettoken/$', views.gettoken, name='gettoken'),
  url(r'^view/tasks$',views.viewwork,name="viewwork"),
  url(r'^createtask/$', views.createtask, name='createtask'),
  url(r'^createtask/taskset$', views.taskset, name='taskset'),
]