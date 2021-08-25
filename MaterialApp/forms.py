from django import forms
from .models import Material, MaterialRequest

class AddMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'type_of', 'quantity', 'model']

class MaterialRequestForm(forms.ModelForm):
    class Meta:
        model = MaterialRequest
        exclude=('user','status',)
class ApprovedMaterial(forms.ModelForm):
    class Meta:
        model = MaterialRequest
        fields = ['status']
