from django.contrib import admin
from .models import MaterialRequest, Material

admin.site.register(Material)
admin.site.register(MaterialRequest)
