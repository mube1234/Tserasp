from django import template
from Trequest.views import dep_notifications_count, scho_notifications_count, tsho_notifications_count
# To be a valid tag library, the module must contain a module-level variable named register that is a template.
# Library instance, in which all the tags and filters are registered
register=template.Library()
@register.inclusion_tag('Trequest/notifications_dep.html')
def dep_notification_number():
    return { 'dep_notifications_number':dep_notifications_count()   }
       
@register.inclusion_tag('Trequest/notifications_schoool.html')
def scho_notification_number():
    return { 'scho_notifications_number':scho_notifications_count()   }

@register.inclusion_tag('Trequest/notifications_tsho.html')
def tsho_notification_number():
    return { 'tsho_notifications_number':tsho_notifications_count()   }
       