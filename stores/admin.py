from django.contrib import admin
from .models import Store, ReviewStore

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'twitter_handle', 'instagram_handle', 'owner', 'date_created']
    prepopulated_fields = {'slug': ('name', )}


class ReviewStoreAdmin(admin.ModelAdmin):
    list_display = ['store', 'email', 'name', 'review', 'rating']

admin.site.register(Store, StoreAdmin)

admin.site.register(ReviewStore, ReviewStoreAdmin)

