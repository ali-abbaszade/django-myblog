from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView, CreateView
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import PostSearchForm
from .models import Post


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "body", "status", "image", "tags"]
    template_name = "blog/write_post.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your post created successfully.")
        return super().form_valid(form)

class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        posts = Post.objects.filter(status="published")
        return posts

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"


class PostSingleView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/single.html"


class TagListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(tags__name__in=[self.kwargs["slug"]])

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/tag-post-list-elements.html"
        return "blog/tags.html"

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["slug"] = self.kwargs["slug"]
        return context


class PostSearchView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"
    form_class = PostSearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data["search"]
            return Post.objects.filter(
                Q(title__icontains=query) | Q(tags__name__in=[query])
            )

        return []

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/search-post-list-elements.html"
        return "blog/search.html"
