from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = (
    url(r'^about', views.about, name='about'),
    url(r'^contacts', views.contacts, name='contacts'),
    url(r'^fund', views.fund, name="fund"),
    url(r'^test', views.GalleryList.as_view(), name="test"),
    url(r'^charity', views.charity, name="charity"),
    url(r'^documents', views.documents, name="documents"),
    url(r'^gallery', views.GalleryList.as_view(), name="gallery"),
    url(r'^team', views.PersonList.as_view(), name="team"),
)