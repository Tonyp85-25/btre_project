from django.contrib import admin
from .models import Country
# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    list_display_links = ('id', 'title')  # which fields are clickable
    list_editable = ('is_active',)  # which field we can edit
    search_fields = ('title', 'currency')
    list_per_page = 25


admin.site.register(Country, CountryAdmin)