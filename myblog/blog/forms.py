from django import forms
from . import models


class PostSearchForm(forms.Form):
    search = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["search"].widget.attrs.update({"class": "form-control"})
