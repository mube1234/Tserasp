from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm, MyUserChangeForm


class MyUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username','first_name','last_name','email', 'phone','school','department', 'role']
    fieldsets = UserAdmin.fieldsets + ( (None, {'fields': ('phone','school','department', 'role',)}),) #this will allow to change these fields in admin module
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Driver)
admin.site.register(Profile)
admin.site.register(TransportRequest)
admin.site.register(Vehicle)
admin.site.register(ApproveRequest)
admin.site.register(Schedule)
admin.site.register(MaterialRequest)
#admin.site.register(AssignedVehicle)
# admin.site.register(TransportRequest)
# admin.site.register(Vehicle)
# admin.site.register(Material)
# admin.site.register(MaterialRequest)