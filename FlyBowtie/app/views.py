from django.shortcuts import render
from django.http import HttpRequest
from django.utils.translation import ugettext as _
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.views.i18n import set_language

def select_lang(request, code):
    request.session[LANGUAGE_SESSION_KEY] = code

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
def team(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/team.html',
        {
            'title': _('Команда'),
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
def media(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/media.html',
        {
            'title': _('Медиагалерея'),
        }
    )