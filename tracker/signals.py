from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Category

@receiver(post_save, sender=User)
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        default_categories = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Others']
        for category_name in default_categories:
            Category.objects.create(name=category_name, user=instance)
