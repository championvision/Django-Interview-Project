from django.conf.urls import url
from sites import views as myapp_views

# Made url sub directories redirections like localhost/summary_average
# by calling related views

urlpatterns = [
    url(r'^sites/$', myapp_views.sites, name='sites'),
    url(r'^summary/$', myapp_views.summary, name='summary'),
    url(r'^summary-average/$',
        myapp_views.summary_average, name='summary-average'),
    url(r'^sites/1/$', myapp_views.demosite, name='demosite'),
    url(r'^sites/2/$', myapp_views.abcsite, name='abcsite'),
    url(r'^sites/3/$', myapp_views.xyzsite, name='xyzsite'),
]
