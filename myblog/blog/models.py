from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=options, default="draft")
    image = models.ImageField(default="blog/default.jpg", upload_to="blog/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("post_single", args=[self.slug])

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    @property
    def vote_ratio(self):
        comments = self.comment_set.all()
        up_votes = comments.filter(vote="up vote").count()
        total_votes = comments.count()
        ratio = (up_votes / total_votes) * 100
        return total_votes, ratio, up_votes

    @property
    def users_leave_comment(self):
        return self.comment_set.all().values_list("user__id", flat=True)


class Comment(models.Model):
    VOTE_VALUE = [
        ("up vote", "Up Vote"),
        ("down vote", "Down Vote"),
    ]
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    vote = models.CharField(max_length=30, choices=VOTE_VALUE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["post", "user"], name="unique comment")
        ]

    def __str__(self):
        return str(self.user)
