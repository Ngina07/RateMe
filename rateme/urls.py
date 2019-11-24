from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
# from django.views.generic import RedirectView

urlpatterns=[
     url('^$',views.welcome,name = 'welcome'),
     url(r'^sites/(\d+)$', views.project, name='project'),
     url(r'^upload/$', views.upload_project, name='upload'),
     url(r'^search/$', views.search, name='search_results'),
     
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)