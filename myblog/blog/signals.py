from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from . import models


@receiver(pre_save, sender=models.Post)
def update_slug_post(sender, instance, **kwargs):
    slug = slugify(instance.title)
    instance.slug = slugify(slug)
