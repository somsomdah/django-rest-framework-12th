from django import contrib

from .forms import UserCreationForm, UserChangeForm
from .models import *


class UserAdmin(contrib.auth.admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('code','name', 'is_staff', 'is_active',)
    list_filter = ('code','name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('code','name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('code', 'name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('code',)
    ordering = ('code',)


contrib.admin.site.register(User,UserAdmin)