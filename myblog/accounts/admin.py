from django.contrib import admin
from .models import Profile

from django_summernote.admin import SummernoteModelAdmin


class ProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ["about"]

admin.site.register(Profile, ProfileAdmin)