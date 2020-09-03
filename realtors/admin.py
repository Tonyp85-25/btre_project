from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')  # fields displayed
    list_display_links = ('id', 'name')  # which fields are clickable
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
