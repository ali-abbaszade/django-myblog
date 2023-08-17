from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()

@receiver(pre_save, sender=models.Post)
def update_slug_post(sender, instance, **kwargs):
    slug = slugify(instance.title)
    instance.slug = slugify(slug)


@receiver(post_save, sender=User)
def create_profile_user(sender, instance, created,  **kwargs):
    if created:
        models.Profile.objects.create(
            owner=instance,
        )
    