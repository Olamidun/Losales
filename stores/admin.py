from django.contrib import admin
from .models import Store

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'twitter_handle', 'instagram_handle', 'owner', 'date_created']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Store, StoreAdmin)