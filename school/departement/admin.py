from django.contrib import admin
from .models import Departement

# Register your models here.
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'description')
