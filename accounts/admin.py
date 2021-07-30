from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ElearningUserCreationForm, ElearningUserChangeForm
from .models import ElearningUser

class ElearningUserUserAdmin(UserAdmin):
    add_form = ElearningUserCreationForm
    form = ElearningUserChangeForm
    model = ElearningUser
    list_display = ['email', 'username','role']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'role', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'eLearning User',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'role',
                ),
            },
        ),
    )


admin.site.register(ElearningUser, ElearningUserUserAdmin)
