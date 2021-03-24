from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account, Customer
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=Account)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=Account)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()