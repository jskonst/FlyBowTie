from django.contrib import admin
from .models import Person, Position

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    model = Person

class PositonAdmin(admin.ModelAdmin):
    model = Position

admin.site.register(Person)
admin.site.register(Position)