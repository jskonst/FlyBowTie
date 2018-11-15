from django.contrib import admin
from .models import Person, Position

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'img')


class PositonAdmin(admin.ModelAdmin):
    model = Position

admin.site.register(Person, PersonAdmin)
admin.site.register(Position, PositonAdmin)