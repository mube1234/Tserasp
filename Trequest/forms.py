from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *
class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'school', 'department', 'role')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'school', 'department', 'role',)


class VehicleRegisterForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('adder',)
        widgets = {
            'adder': forms.Select(attrs={'type': ''})
        }


class MakeRequestForm(forms.ModelForm):
    class Meta:
        model = TransportRequest
        exclude = ('passenger',)
        widgets = {

            'start_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'),
                                        attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                               'type': 'date'}),
            'status': forms.TextInput(attrs={'type': 'hidden'}),
            'status2': forms.TextInput(attrs={'type': 'hidden'}),
            'status3': forms.TextInput(attrs={'type': 'hidden'}),

        }
        help_texts = {
            'passenger_numbers': "* Enter the number of Passengers that will go with you",
            'reason': "* Reason of your trip",
            'list_of_passengers':'list of the passengers that go with you'
        }


class ApproveRequestForm(forms.ModelForm):
    class Meta:
        model = ApproveRequest
        exclude = ('user',)
        widgets = {
            'user': forms.TextInput(attrs={'': ''}),
        }


class DepartmentApproveForm(forms.ModelForm):
    class Meta:
        model = TransportRequest
        fields = ['status2']
        widgets = {

            'status2': forms.Select(),
        }


class SchoolApproveForm(forms.ModelForm):
    class Meta:
        model = TransportRequest
        fields = ['status3']
        widgets = {

            'status3': forms.Select(),
        }


class TshoApproveForm(forms.ModelForm):
    class Meta:
        model = TransportRequest
        fields = ['status2']
        widgets = {

            'status2': forms.TextInput(attrs={'type': 'hidden'}),
        }


class EmailSendForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = ApproveRequest


class CreateScheduleForm(forms.ModelForm):
    class Meta:
        exclude = ('author',)
        model = Schedule
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'),
                                    attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                           'type': 'date'}),

        }


####Naol
class AddMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'type_of', 'quantity']







# class MaterialRequestForm(forms.ModelForm):
#     class Meta:
#         model = MaterialRequest
#         fields = ['name', 'RequestedBy', 'OldMaterial',
#                   'NewMaterial', 'Amount', 'status']
















#####end who naol done for this project.
# class PassengerRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Passenger
#         fields = '__all__'
# password_regex = RegexValidator(
#     regex=r'^\S{6,1024}',
#     message='password must be at least 6 character'
# )
# password = forms.CharField(
#     validators=[password_regex],
#     max_length=1024,
#     widget=forms.PasswordInput(),
#     help_text='*Enter your password minimum 6 character',
#     label='Password'
# )
# confirm_password = forms.CharField(
#     max_length=1024,
#     widget=forms.PasswordInput(),
#     help_text='*Confirm your password'
# )


# fields = ['first_name', 'last_name', 'phone', 'email', 'department', 'sex', 'password', 'confirm_password']
# widgets = {
#     'first_name': forms.TextInput(attrs={'class': 'form-control', }),
#     'last_name': forms.TextInput(attrs={'class': 'form-control', }),
#     'phone': forms.TextInput(),
#     'email': forms.EmailInput(),
#     'department': forms.TextInput(),
#     'sex': forms.Select(),
#     'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#     'confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
#
# }
# help_texts = {
#     'phone': "* Your phone number must enter in correct format.",
#     'confirm_password': "* Your password can’t be entirely numeric.",
# }
#
# def clean(self):
#     cleaned_data = super(PassengerRegistrationForm, self).clean()
#     password = cleaned_data.get('password')
#     confirm_password = cleaned_data.get('confirm_password')
#     if password and confirm_password:
#         if password != confirm_password:
#             raise forms.ValidationError('Password mismatch')
#
#     return confirm_password
