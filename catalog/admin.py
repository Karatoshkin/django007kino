from django.contrib import admin
from .models import *


admin.site.register(Genre)
# admin.site.register(Director)
# admin.site.register(Actor)
admin.site.register(AgeRate)
# admin.site.register(Status)
# admin.site.register(Film)
admin.site.register(Country)

class Actoradmin(admin.ModelAdmin):
    list_display = ("fname","lname","born")
    list_display_links = ("fname","lname")
admin.site.register(Actor,Actoradmin)

class Directoradmin(admin.ModelAdmin):
    list_display = ("fname","lname")
    list_display_links = ("fname","lname")
admin.site.register(Director,Directoradmin)

class Stinline(admin.TabularInline):
    model = Film

class Statusadmin(admin.ModelAdmin):
    inlines = [Stinline]
admin.site.register(Status,Statusadmin)


class Filmadmin(admin.ModelAdmin):
    list_display = ('title','year','director','display_actors')
    list_filter = ('status', 'genre','rating')
    fieldsets = (('О фильме',{'fields':('title','summary','actor')}),("Рейтинг",{'fields':('rating','ager','status')}))
admin.site.register(Film,Filmadmin)