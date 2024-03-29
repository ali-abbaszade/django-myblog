from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import PostSearchForm
from .models import Post, Comment
from . import forms
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = forms.PostForm
    template_name = "blog/write_post.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your post created successfully.")
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = forms.PostForm
    template_name = "blog/update_post.html"

    def get_success_url(self):
        if self.object.status == "draft":
            messages.success(self.request, "Your post updated successfully.")
            return reverse_lazy("home")
        else:
            messages.success(self.request, "Your post updated successfully.")
            return reverse_lazy("post_single", args=[self.object.slug])


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("home")


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


def post_single(request, slug):
    post = Post.objects.get(slug=slug)
    form = forms.CommentForm()
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("post_single", slug=post.slug)

    context = {"form": form, "post": post} 
    hit_count = get_hitcount_model().objects.get_for_object(post)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits += 1
        hitcontext['total_hits'] = hits   
    return render(request, "blog/single.html", context)


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
