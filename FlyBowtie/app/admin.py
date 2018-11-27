from django.contrib import admin
from .models import Person, Position, MediaList, CarouselList

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'img')

class PositonAdmin(admin.ModelAdmin):
    model = Position

class MediaListAdmin(admin.ModelAdmin):
    model = MediaList

class CarouselListAdmin(admin.ModelAdmin):
    model = CarouselList


admin.site.register(Person, PersonAdmin)
admin.site.register(Position, PositonAdmin)
admin.site.register(MediaList, MediaListAdmin)
admin.site.register(CarouselList, CarouselListAdmin)