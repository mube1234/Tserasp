from django.contrib.auth.admin import UserAdmin
from django.db.models.signals import post_save,pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, MyUser, Notifications, ActivityLog ,TransportRequest,Schedule,Material,Vehicle

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
        #data='Schedule created to ' + str(instance.place)+' assigned to driver '+str(instance.driver.user.first_name + "  "+ instance.driver.user.last_name)+' is added '
        ActivityLog.objects.create(created_by=instance,instances="Schedule",log_object=instance.place,action="Addition")
    else:
        ActivityLog.objects.create(created_by=instance,instances="Schedule",log_object=instance.place,action="Updated")

@receiver(pre_delete,sender=Schedule)
def log_cancel_schedule(sender,instance, **kwargs):
    ActivityLog.objects.create(created_by=instance,instances="Schedule",log_object=instance.place,action="Deleted")



  # material log      
@receiver(post_save, sender=Material)
def log_material(sender,instance,created, **kwargs):
    if created:
        ActivityLog.objects.create(created_by=instance,instances="Material",log_object=str(instance.quantity),action="Addition")
    else:
        ActivityLog.objects.create(created_by=instance,instances="Material",log_object=str(instance.quantity),action="Updated")

@receiver(pre_delete,sender=Material)
def log_delete_material(sender,instance, **kwargs):
    ActivityLog.objects.create(created_by=instance,instances="Material",log_object=instance.name,action="Deleted")



# vehicle log
@receiver(post_save,sender= Vehicle)
def log_vehicle(sender,instance,created, **kwargs):
    if created:
        ActivityLog.objects.create(created_by=str(instance.adder.first_name + "  "+ instance.adder.last_name),instances="Vehicle",log_object= str(instance.plate_number),action="Addition")
    else:
        ActivityLog.objects.create(created_by=str(instance.adder.first_name + "  "+ instance.adder.last_name),instances="Vehicle",log_object= str(instance.plate_number),action="Updated")

@receiver(pre_delete,sender=Vehicle)
def log_delete_vehicle(sender,instance, **kwargs):
    ActivityLog.objects.create(created_by=str(instance.adder.first_name + "  "+ instance.adder.last_name),instances="Vehicle",log_object=instance.plate_number,action="Deleted")


# user log
@receiver(post_save,sender= MyUser)
def log_add_user(sender,instance,created, **kwargs):
    if created:
        ActivityLog.objects.create(created_by=str(instance.first_name)+' ' +str(instance.last_name),instances='MyUser',log_object=str(instance.role),action='Addition')
    #else:
      #  ActivityLog.objects.create(created_by=str(instance.first_name)+' ' +str(instance.last_name),instances='MyUser',log_object=str(instance.role),action='Updated')
@receiver(pre_delete,sender=MyUser)
def log_delete_user(sender,instance, **kwargs):
    ActivityLog.objects.create(created_by=str(instance.first_name)+' ' +str(instance.last_name),instances='MyUser',log_object=str(instance.role),action='Deletion')

# trasport request log

@receiver(post_save,sender= TransportRequest)
def log_request_(sender,instance,created, **kwargs):
    if created:
        ActivityLog.objects.create(created_by=str(instance.passenger.first_name)+' ' +str(instance.passenger.last_name),instances='TransportRequest',log_object=str(instance.destination),action='Addition')
    else:
        ActivityLog.objects.create(created_by=str(instance.passenger.first_name)+' ' +str(instance.passenger.last_name),instances='TransportRequest',log_object=str(instance.destination),action='Updated')

@receiver(pre_delete,sender=TransportRequest)
def log_cancel_transport_request(sender,instance, **kwargs):
    ActivityLog.objects.create(created_by=instance.passenger,instances='TransportRequest',log_object=str(instance),action='Deletion')
