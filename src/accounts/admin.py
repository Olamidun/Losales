from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Register your models here.

class AccountAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['email', 'first_name', 'last_name', 'date_joined', 'is_admin', 'is_staff', 'is_dispatch_rider']
    search_fields = ['first_name','last_name', 'email',]
    readonly_fields = ['date_joined', 'last_login']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_joined',)}),
        ('Permissions', {'fields': ('is_admin', 'is_verified', 'is_active', 'is_staff', 'is_dispatch_rider',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','email', 'password1', 'password2'),
        }),
        ('Permissions', {'fields': ('is_admin', 'is_verified', 'is_active', 'is_staff', 'is_dispatch_rider', )}),
    )
    ordering = ('email', )

admin.site.register(Account, AccountAdmin)