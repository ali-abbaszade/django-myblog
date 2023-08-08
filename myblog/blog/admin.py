from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

from .models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)


admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)
