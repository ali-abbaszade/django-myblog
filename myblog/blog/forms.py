from django import forms
from . import models


class PostSearchForm(forms.Form):
    search = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["search"].widget.attrs.update({"class": "form-control"})


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "body", "status", "image", "tags"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control form-control-lg"})


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ["vote", "body"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
