from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    # this passes test_users_listed
    ordering = ['id']
    list_display = ['email', 'name']

    # this passes test_user_page_change
    fieldsets = (
        (
            None,
            {'fields': ('email', 'password')}
        ),
        (
            _('Personal Info'),
            {'fields': ('name',)}
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            _('Important dates'),
            {'fields': ('last_login',)}
        ),
    )

    # this passes test_create_user_page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)

'''NOTE:
Here is a full example of how to register this custom user model
with Django's admin

docs.djangoproject.com/en/4.0/topics/auth/customizing/#a-full-example
'''

'''NOTE:
Only the 1st argument for admin.site.register() is mandatory.
The 2nd argument (optional) is to configure how the model is
managed in the admin site.

In this case if the 2nd argument is not provided, the information
of the user would be showed in raw text, for example the password
woud appear without hashing.
'''

'''NOTE:
About fieldsets, check:

docs.djangoproject.com
/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
'''
