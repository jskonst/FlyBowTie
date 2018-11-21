from django.shortcuts import render
from django.http import HttpRequest
from django.utils.translation import ugettext as _
from django.views.generic import ListView
from .models import Person, MediaList


class PersonList(ListView):
    model = Person
    context_object_name = 'persons'
    template_name = 'app/team.html'

class GalleryList(ListView):
    model = MediaList
    context_object_name = 'gallery'
    template_name = 'app/media.html'

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': _('Полёт бабочки'),
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': _('О проекте'),
        }
    )

def contacts(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contacts.html',
        {
            'title': _('Контакты'),
        }
    )
def fund(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fund.html',
        {
            'title': _('Фонд "Доброе дело"'),
        }
    )
def charity(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/charity.html',
        {
            'title': _('Благотворительность'),
        }
    )
def documents(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/documents.html',
        {
            'title': _('Документы'),
        }
    )