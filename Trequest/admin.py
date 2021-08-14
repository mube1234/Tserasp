from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm, MyUserChangeForm

# for activity log
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe
# end


class MyUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username', 'first_name', 'last_name',
                    'email', 'phone', 'school', 'department', 'role']
    # this will allow to change these fields in admin module
    fieldsets = UserAdmin.fieldsets + \
        ((None, {'fields': ('phone', 'school', 'department', 'role',)}),)


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Driver)
admin.site.register(Profile)
admin.site.register(TransportRequest)
admin.site.register(Vehicle)
admin.site.register(ApproveRequest)
admin.site.register(Schedule)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Material)
admin.site.register(Notifications)
admin.site.register(MaterialRequest)
admin.site.register(DriverEvaluation)
admin.site.register(feedback)
admin.site.register(VehicleType)


#  for log entry
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' %
                        (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return mark_safe(link)
    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"
