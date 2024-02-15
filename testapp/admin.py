from django.contrib import admin
from testapp.models import movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['rdate','moviename','actor','actress','rating']

admin.site.register(movie,MovieAdmin)
