from django.contrib import admin
from django.urls import path
from TaskCreater import views
from django.conf.urls import url, include
urlpatterns = [
    # Invoke the home view in the tutorial app by default
    url(r'^$', views.home, name='home'),
    # Defer any URLS to the /tutorial directory to the tutorial app
    url(r'^taskcreater/', include('TaskCreater.urls', namespace='TaskCreater')),
    url(r'^admin/', admin.site.urls),
]
