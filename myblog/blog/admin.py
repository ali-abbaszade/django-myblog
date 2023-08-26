from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Comment


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.unregister(Group)
