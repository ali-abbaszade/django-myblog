from django import template

from myblog.blog.models import Post

register = template.Library()


@register.inclusion_tag("blog/components/splash.html")
def last_post():
    latest_post = Post.objects.filter(status='published').last()
    return {"latest_post": latest_post}
