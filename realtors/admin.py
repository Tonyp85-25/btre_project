from django.contrib import admin
from .models import Realtor
# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date', 'country')  # fields displayed 'country'
    list_display_links = ('id', 'name')  # which fields are clickable
    search_fields = ('name', )  # 'country'
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)

