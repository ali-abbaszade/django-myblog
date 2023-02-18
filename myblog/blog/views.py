from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Post


class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"


class PostSingleView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/single.html"
