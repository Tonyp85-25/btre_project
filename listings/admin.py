from django.contrib import admin
from .models import Listing
# Register your models here.

# we can extend the dispaly in admin area and chose which information is displayed and how we can act on


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')  # fields displayed
    list_display_links = ('id', 'title')  # which fields are clickable
    list_filter = ('realtor',)  # adding a filter
    list_editable = ('is_published',)  # which field we can edit
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
