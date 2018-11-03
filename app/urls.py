from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = (
    #url(r'^', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^contacts', views.contacts, name='contacts'),
    url(r'^fund', views.fund, name="fund"),
    url(r'^team', views.team, name="team"),
    url(r'^charity', views.charity, name="charity"),
    url(r'^documents', views.documents, name="documents"),
    url(r'^media', views.media, name="media"),
)