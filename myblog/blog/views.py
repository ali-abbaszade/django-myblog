from django.views.generic import DetailView, ListView

from .forms import PostSearchForm
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
            return Post.objects.filter(title__icontains=query)

        return []

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/search-post-list-elements.html"
        return "blog/search.html"
