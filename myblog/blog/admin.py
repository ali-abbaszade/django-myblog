from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Profile


class ProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ["about"]


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Group)
