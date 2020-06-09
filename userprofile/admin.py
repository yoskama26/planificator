from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserProfileCreationForm, UserProfileChangeForm
from .models import UserProfile

class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ['email', 'username']
    fieldsets = UserAdmin.fieldsets + (
            ('Profile', {'fields': ('service',)}),)

admin.site.register(UserProfile, UserProfileAdmin)