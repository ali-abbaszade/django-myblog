from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Post

admin.site.register(Post)
admin.site.unregister(Group)
