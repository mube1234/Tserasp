from django import template
from MaterialApp.views import alert_count
# To be a valid tag library, the module must contain a module-level variable named register that is
# a template.
# Library instance, in which all the tags and filters are registered
register=template.Library()
@register.inclusion_tag('MaterialApp/total_min_material.html')
def alert_number():
    return { 'totalalert': alert_count()   }
       
