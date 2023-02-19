from django import template
from django.shortcuts import get_object_or_404

from myblog.blog.models import Post

register = template.Library()


@register.inclusion_tag("blog/components/related-posts.html")
def related(slug):
    post = get_object_or_404(Post, slug=slug, status="published")
    related_posts = Post.objects.filter(author=post.author)[:5]
    return {"related_posts": related_posts, "post": post}
