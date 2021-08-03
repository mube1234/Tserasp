from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from TSERASP import settings


class MyUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    ROLE = (
        ('Passenger', 'Passenger'),
        ('TSHO', 'TSHO'),
        ('Mechanic', 'Mechanic'),
        ('Driver', 'Driver'),
        ('StoreManager', 'Store Manager'),
        ('SchoolDean', 'School Dean'),
        ('DepartmentHead', 'Department Head'),
        ('VicePresident', 'Vice President'),
    )
    School = (
        ('SOEEC', 'SOEEC'),
        ('SOMCME', 'SOMCME'),
        ('SOCEA', 'SOCEA'),
        ('SOANS', 'SOANS'),
    )
    Department = (
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EPCE', 'EPCE'),
        ('MCE', 'MCE'),
        ('MSE', 'MSE'),
        ('CHE', 'CHE'),
        ('CE', 'CE'),
        ('WRE', 'WRE'),
        ('ARCH', 'ARCH'),
        ('Maths', 'Maths'),
        ('Pysics', 'Pysics'),
        ('Chemistry', 'Chemistry'),
        ('Bio', 'Bio'),
        ('Geology', 'Geology')
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10,15}$',
        message='Phone number must be entered in the format : 0987654321 or +251987654321 up to 15 digits allowed'
    )
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    department = models.CharField(max_length=200, choices=Department, null=True, blank=True)
    school = models.CharField(max_length=200, choices=School, null=True, blank=True)
    role = models.CharField(max_length=200, choices=ROLE)
    date_registered = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.username
    # mobile_number = models.CharField(max_length=10, unique=True)
    # birth_date = models.DateField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='passenger')
    sex = models.CharField(max_length=200, choices=(('male', 'male'), ('female', 'female')), null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.user.first_name + "  "+ self.user.last_name + "  " + 'detail'


# konrad zuse =1938=world fully programmable computer = german
# 1960
#
# 1971 john draper =phone call

class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee')
    occupation = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=100, null=True)
    house_no = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username


class TransportRequest(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    )
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_request')
    start_from = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    reason = models.TextField(max_length=400)
    passenger_numbers = models.PositiveIntegerField(default=1)
    list_of_passengers=models.TextField(max_length=400,null=True,blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, default='Pending', choices=STATUS)
    status2 = models.CharField(max_length=200, default='Pending', choices=STATUS)
    status3 = models.CharField(max_length=200, default='Pending', choices=STATUS)

    def __str__(self):
        return self.start_from + ' to ' + self.destination


class Vehicle(models.Model):
    STATUS = (
        ('Not Occupied', 'Not Occupied'),
        ('Occupied', 'Occupied'),
    )
    type_of_vehicle = (
        ('minibus', 'minibus'),
        ('bus', 'bus'),
        ('kobra', 'kobra'),
        ('ambulance', 'ambulance')
    )
    adder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='add')
    vehicle_type = models.CharField(max_length=200, choices=type_of_vehicle)
    plate_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=200, choices=STATUS, default='Not Occupied')
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, null=True,blank=True)
    date_entered = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.plate_number


# class AssignedVehicle(models.Model):

#      my_vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
#      date_recieved=models.DateTimeField(auto_now_add=True)
#      def __str__(self):
#         return  self.my_vehicle.vehicle_type 

class ApproveRequest(models.Model):
    user = models.OneToOneField(TransportRequest, on_delete=models.CASCADE)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    time = models.CharField(max_length=200, default='06:00am')

    def __str__(self):
        return self.user.start_from + ' to ' + self.user.destination + ' Approved '


class Schedule(models.Model):
    select = (
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='adder')
    shift = models.CharField(max_length=100, choices=select)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver_name')
    service_type = models.CharField(max_length=200)
    date = models.DateField()
    time = models.CharField(max_length=200)
    place = models.CharField(max_length=200)

    def __str__(self):
        return self.service_type
#     by naol
class Material(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete= models.SET_NULL)
    name=models.CharField(max_length=200)
    type_of = models.CharField(max_length=200)
    quantity=models.PositiveIntegerField()
    date_created = models.DateField( auto_now_add=  True, null=True)
    updated_at = models.DateTimeField(null=True)


# class Material(models.Model):
#     user = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='matregister')
#     name=models.CharField(max_length=200)
#     type = models.CharField(max_length=200)
#     quantity=models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
# # class Schedule(models.Model):
# #     service_type=models.CharField(max_length=)
# #
# # class ReassignSchedule(models.Model):
# #     re_assigned_to=models.ForeignKey(Schedule,on_delete=models.CASCADE)
# class MaterialRequest(models.Model):
#     STATUS = (('Pending','Pending'),
#             ('Approved','Approved'),)
#     user=models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='matrequest')
#     name = models.CharField(max_length=200)
#     type = models.CharField(max_length=200)
#     quantity = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=200, choices=STATUS, default='Pending')
#
#     def __str__(self):
#         return self.name
# # class RepairedVehicle(models.Model):
# # class Profile(models.Model):
# # class Evaluation(models.Model):
