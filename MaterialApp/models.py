from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from TSERASP import settings
from datetime import date
from Trequest.models import Vehicle

class Material(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200,unique=True)
    model = models.CharField(max_length=200 ,null=True)
    type_of = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    date_created = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class MaterialRequest(models.Model):
    # material name
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete= models.SET_NULL)
    new_material_name = models.ForeignKey(Material, on_delete=models.DO_NOTHING, null=True, related_name='new_material')
    new_material_model = models.CharField(max_length=200)
    quantity_of_new = models.PositiveIntegerField()
    #old_material_name = models.ForeignKey(Material, on_delete=models.DO_NOTHING, null=True, related_name='old_material')
    # old_material_name = models.ForeignKey(Material, on_delete=models.DO_NOTHING, null=True, related_name='old_material')
    quantity_of_old=models.PositiveIntegerField()
    old_material_model=models.CharField(max_length=200)
    vehicle_model = models.ForeignKey(Vehicle, max_length=200, on_delete=models.DO_NOTHING, null=True)
    condition = models.CharField(max_length=200,choices=(('Reusable', 'reusable'), ('Usable', 'usable')), null=True,blank=True)
    status = models.CharField(max_length=200, default='Pending', choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.new_material_name.name

    class Meta:
        ordering = ['-id']   