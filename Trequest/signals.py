from django.contrib.auth.admin import UserAdmin
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, MyUser, Notifications, TransportRequest

@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('User profile created')


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    print('Passenger updated')

@receiver(post_save, sender=TransportRequest)
def create_notifications(sender,instance, created, **kwargs):
    if created:
        Notifications.objects.create(request_id=instance)