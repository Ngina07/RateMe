from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
# from django.views.generic import RedirectView

urlpatterns=[
     url('^$',views.welcome,name = 'welcome'),
     url(r'^upload/$', views.upload_project, name='upload'),
]