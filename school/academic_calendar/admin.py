from django.contrib import admin
from .models import Holiday

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_school_closed')
    list_filter = ('is_school_closed',)
    search_fields = ('title',)