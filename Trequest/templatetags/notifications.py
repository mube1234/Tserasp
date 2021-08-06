from django import template
from Trequest.views import dep_notifications_count
# To be a valid tag library, the module must contain a module-level variable named register that is a template.
# Library instance, in which all the tags and filters are registered
register=template.Library()
@register.inclusion_tag('Trequest/notifications.html')
def dep_notification_number():
    return { 'dep_notification_number':dep_notifications_count()   }
       
# @register.inclusion_tag('Trequest/notifications.html')
# def dep_notifications_number():
#     return { 'scho_notification_number':scho_notifications_count()   }

# @register.inclusion_tag('Trequest/notifications.html')
# def dep_notifications_number():
#     return { 'tsho_notification_number':tsho_notifications_count()   }
       