from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Patient


# @receiver(post_save, sender=Patient)
# def create_patient(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(user=instance)