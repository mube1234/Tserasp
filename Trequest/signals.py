from django.contrib.auth import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.signals import post_save,pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import * #ActivityLog, Profile, MyUser, Notifications, Schedule,ActivityLog, TransportRequest

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

  # Activity Log done by Abdi Dasta 
  # 
  # schedule log     
@receiver(post_save, sender=Schedule)
def log_schedule(sender,instance,created, **kwargs):
    if created:
        data='Schedule created to ' + str(instance.place)+' assigned to driver '+str(instance.driver.user.first_name + "  "+ instance.driver.user.last_name)+' is added '
        ActivityLog.objects.create(created_by=instance,instances=data)
    else:
        ActivityLog.objects.create(created_by=instance,instances="Schedule updated")

  # material log      
@receiver(post_save, sender=Material)
def log_material(sender,instance,created, **kwargs):
    if created:
        ActivityLog.objects.create(created_by=instance,instances=str(instance.quantity)+' amount of '+ str(instance.name)+' is added to store' )
    else:
        ActivityLog.objects.create(created_by=instance,instances=str(instance.quantity)+' amount of '+ str(instance.name)+' is updated to store' )
# vehicle log
@receiver(post_save,sender= Vehicle)
def log_vehicle(sender,instance,created, **kwargs):
    if created:
        ActivityLog.objects.create(created_by=str(instance.adder.first_name + "  "+ instance.adder.last_name),instances='Vehicle with '+ str(instance.plate_number)+ ' plate number with driver '+str(instance.driver.user.first_name + "  "+ instance.driver.user.last_name)+' is registered')

# user log
@receiver(post_save,sender= MyUser)
def log_add_user(sender,instance,created, **kwargs):
    if created:
        ActivityLog.objects.create(created_by=str(instance.first_name)+' ' +str(instance.last_name),instances='Added to the User as '+str(instance.role))
@receiver(pre_delete,sender=MyUser)
def log_delete_user(sender,instance, **kwargs):
    ActivityLog.objects.create(created_by=str(instance.first_name)+' ' +str(instance.last_name),instances=' This user is Deleted')

# trasport request log
@receiver(pre_delete,sender=TransportRequest)
def log_cancel_transport_request(sender,instance, **kwargs):
    ActivityLog.objects.create(created_by=instance.passenger,instances=str(instance.passenger)+' cancel his from '+str(instance))