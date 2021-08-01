#from Tserasp import Trequest
from sys import path_hooks
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from Trequest.forms import *
from django.core.mail import send_mail
from .filters import MaterialFilter, UserFilter
import random
import string
#adding by Naol
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
class Requestpdf(ListView):
    model = TransportRequest
    template_name = 'Trequest/invoice.html'
def request_pdf(request, *args , **kwargs) :
    pk = kwargs.get('pk')
    requestpdf = get_object_or_404(TransportRequest, pk = pk)
    template_path = 'Trequest/invoice.html'
    context = {'requestpdf': requestpdf}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #If download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if display:
    response['Content-Disposition'] = 'filename="report.pdf"' 
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Incorrect username or password!')

    return render(request, 'Trequest/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    schedule = Schedule.objects.all().order_by('-date')
    approved_request = TransportRequest.objects.filter(status='Approved')
    tsho_pending_request = TransportRequest.objects.filter(status='Pending', status2='Approved', status3='Approved')
    dep_pending_request = TransportRequest.objects.filter(status2='Pending',
                                                          passenger__department=request.user.department)
    sch_pending_request = TransportRequest.objects.filter(status3='Pending', status2='Approved',
                                                          passenger__school=request.user.school)
    app = approved_request.count()
    tsho_pend = tsho_pending_request.count()
    dep_pend = dep_pending_request.count()
    sch_pend = sch_pending_request.count()
    vehicle = Vehicle.objects.all()
    vehicle_count = vehicle.count()
    context = {'schedule': schedule,
               'vehicle_count': vehicle_count,
               'app': app,
               'tsho_pend': tsho_pend,
               'dep_pend': dep_pend,
               'sch_pend': sch_pend
               }
    return render(request, 'Trequest/index.html', context)


@login_required(login_url='login')
def view_request(request):
    return render(request, 'Trequest/view_request.html')


@login_required(login_url='login')
def vehicle_management(request):
    vehicle = Vehicle.objects.all()
    context = {'vehicle': vehicle}
    return render(request, 'Trequest/vehicle_management.html', context)
@login_required(login_url='login')
def history(request):
     return render(request, 'Trequest/history.html')

def edit_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method == 'POST':
        form = VehicleRegisterForm(request.POST, instance=vehicle)
        if form.is_valid():
            alert = 1
            form.save()
            messages.success(request, 'Vehicle updated Successfully!')
            return redirect('vehicle-manage')
        else:
            alert=0
    else:
        alert = None
        form = VehicleRegisterForm(instance=vehicle)

    context = {'form': form,
               'alert':alert}
    return render(request, 'Trequest/update_vehicle.html', context)


@login_required(login_url='login')
def material_management(request):
    return render(request, 'Trequest/material_management.html')


@login_required(login_url='login')
@login_required(login_url='login')
def profile(request):
    return render(request, 'Trequest/profile.html')


def create_account(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            username = 'tserasp'.join(random.choice(string.ascii_uppercase + string.digits) for x in range(2))
            instance = user_form.save(commit=False)
            instance.username = username
            instance.save()
            role = user_form.cleaned_data.get('role')
            if role == 'Driver':
                Driver.objects.create(user=instance)
            messages.success(request, 'Account Created Successfully!')
            return redirect('account')
    else:
        user_form = UserRegistrationForm()
    context = {'user_form': user_form}
    return render(request, 'Trequest/register.html', context)

def delete_account(request,id):
    account=get_object_or_404(MyUser,id=id)
    account.delete()
    messages.success(request, 'Account deleted Successfully!')
    return redirect('account')
def delete_vehicle(request,id):
    veh=get_object_or_404(Vehicle,id=id)
    veh.delete()
    messages.success(request, 'Vehicle deleted Successfully!')
    return redirect('vehicle-manage')
@login_required(login_url='login')
def make_request(request):
    form = MakeRequestForm()
    if request.method == 'POST':
        form = MakeRequestForm(request.POST)
        if form.is_valid():
            # Because your model requires that user is present, we validate the form and 
            # save it without commiting, manually assigning the user to the object and resaving
            obj = form.save(commit=False)
            obj.passenger = request.user
            obj.save()
            messages.success(request, 'Request sent Successfully!')
            return redirect('my-request')
    else:
        form = MakeRequestForm()
    context = {'form': form}
    return render(request, 'Trequest/make_request.html', context)


@login_required(login_url='login')
def vehicle_register(request):
    if request.method == 'POST':
        form = VehicleRegisterForm(request.POST)
        if form.is_valid():
            # Because your model requires that user is present, we validate the form and
            # save it without commiting, manually assigning the user to the object and resaving
            obj = form.save(commit=False)
            obj.adder = request.user
            obj.save()
            messages.success(request, 'Vehicle registered Successfully!')
            return redirect('vehicle-register')
    else:
        form = VehicleRegisterForm()
    context = {'form': form}
    return render(request, 'Trequest/register_vehicle.html', context)


@login_required(login_url='login')
def tsho_assign_request(request, id):
    app = TransportRequest.objects.get(id=id)
    if request.method == 'POST':
        request_form = ApproveRequestForm(request.POST)
        if request_form.is_valid():
            obj = request_form.save(commit=False)
            obj.user = app
            obj.save()
            return send_email(request)
            messages.success(request, 'Request Approve Successfully!')
            return redirect('tsho-view-approved-request')
    else:
        request_form = ApproveRequestForm()
    context = {'form': request_form, 'app': app}
    return render(request, 'Trequest/assign_approved_request.html', context)


def department_view_request(request):
    transport = TransportRequest.objects.filter(status2='Pending').order_by('-created_at')
    context = {'transport': transport}
    return render(request, 'Trequest/department_view_request.html', context)


def department_view_approved_request(request):
    transport = TransportRequest.objects.filter(status2='Approved').order_by('-created_at')
    context = {'transport': transport}
    return render(request, 'Trequest/department_view_approved_request.html', context)


def school_view_request(request):
    transport = TransportRequest.objects.filter(status2='Approved', status3='Pending').order_by('-created_at')
    context = {'transport': transport}
    return render(request, 'Trequest/school_view_request.html', context)


def school_view_approved_request(request):
    transport = TransportRequest.objects.filter(status3='Approved').order_by('-created_at')
    context = {'transport': transport}
    return render(request, 'Trequest/school_view_approved_request.html', context)


def tsho_view_approved_request(request):
    transport = TransportRequest.objects.filter(status='Approved').order_by('-created_at')
    context = {'transport': transport}
    return render(request, 'Trequest/tsho_view_approved_request.html', context)


def tsho_view_approved_request_detail(request, id):
    trans = TransportRequest.objects.get(id=id)
    context = {'trans': trans}
    return render(request, 'Trequest/view_approved_detail.html', context)


def tsho_view_request(request):
    transport = TransportRequest.objects.filter(status2='Approved', status3='Approved', status='Pending').order_by(
        '-created_at')
    context = {'transport': transport}
    return render(request, 'Trequest/tsho_view_request.html', context)


def department_approve_request(request, id):
    approve = get_object_or_404(TransportRequest, id=id)
    if request.method == 'POST':
        form = DepartmentApproveForm(request.POST, instance=approve)
        if form.is_valid():
            form.save()
            return redirect('department-view-approved-request')
    else:
        form = DepartmentApproveForm(instance=approve)
    context = {'form': form, 'approve': approve}
    return render(request, 'Trequest/department_approve_request.html', context)


def tsho_approve_request(request, id):
    approve = get_object_or_404(TransportRequest, id=id)
    if request.method == 'POST':
        form = TshoApproveForm(request.POST, instance=approve)
        if form.is_valid():
            form.save()
            # for sending email to respective user
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            email = request.POST.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [email], fail_silently=False)
            return render(request, 'Trequest/email_sent.html', {'email': email})
    else:
        form = TshoApproveForm(instance=approve)
    context = {'form': form, 'approve': approve}
    return render(request, 'Trequest/tsho_approve_request.html', context)


def school_approve_request(request, id):
    approve = get_object_or_404(TransportRequest, id=id)
    if request.method == 'POST':
        form = SchoolApproveForm(request.POST, instance=approve)
        if form.is_valid():
            form.save()
            return redirect('school-view-approved-request')
    else:
        form = SchoolApproveForm(instance=approve)
    context = {'form': form, 'approve': approve}
    return render(request, 'Trequest/school_approve_request.html', context)


@login_required(login_url='login')
def my_request(request):
    myrequest = TransportRequest.objects.filter(passenger=request.user)
    context = {'myrequest': myrequest}
    return render(request, 'Trequest/myrequest.html', context)
@login_required(login_url='login')
def my_request_detail(request,id):
    myrequest_detail = TransportRequest.objects.get(id=id)
    context = {'myrequest_detail': myrequest_detail}
    return render(request, 'Trequest/my_request_detail.html', context)

def account_management(request):
    account = MyUser.objects.all().order_by('-date_registered')
    total_account = account.count()
    myfilter = UserFilter(request.GET, queryset=account)
    account = myfilter.qs
    context = {'account': account,
               'total_account': total_account,
               'myfilter':myfilter}
    return render(request, 'Trequest/account_management.html', context)


def account_detail(request, username):
    user = Profile.objects.get(user__username=username)
    context = {'user': user}
    return render(request, 'Trequest/user_account_detail.html', context)


# def send_email(request,id):
#     app=TransportRequest.objects.get(id=id)
#     if request.method == 'POST':
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         email = request.POST.get('email')
#         send_mail(subject, message, settings.EMAIL_HOST_USER,
#                   [email], fail_silently=False)
#         return render(request, 'Trequest/email_sent.html', {'email': email})
#
#     return render(request, 'Trequest/assign_approved_request.html', {'app':app})
@login_required(login_url='login')
def create_schedule(request):
    if request.method == 'POST':
        form = CreateScheduleForm(request.POST)
        if form.is_valid():
            # Because your model requires that user is present, we validate the form and
            # save it without commiting, manually assigning the user to the object and resaving
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request, 'Schedule created Successfully!')
            return redirect('index')
    else:
        form = CreateScheduleForm()
    context = {'form': form}
    return render(request, 'Trequest/create_schedule.html', context)


def update_schedule(request, id):
    schedule = Schedule.objects.get(id=id)
    if request.method == 'POST':
        form = CreateScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Schedule updated Successfully')
            return redirect('index')
    else:
        form = CreateScheduleForm(instance=schedule)
    context = {'form': form}
    return render(request, 'Trequest/update_schedule.html', context)


# by naol
def deletematerial(request, pk):
    term = Material.objects.get(id=pk)
    if request.method == 'POST':
        term.delete()
        return redirect('material-manage')
    context = {'term': term}
    return render(request, 'Trequest/deleteMaterial.html', context)


def Updatematerial(request, pk):
    material = Material.objects.get(id=pk)

    form = AddMaterialForm(instance=material)
    if request.method == 'POST':
        form = AddMaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material updated Successfully!')
            return redirect('material-manage')
    context = {'form': form}
    return render(request, 'Trequest/AddMaterialForm.html', context)


def AddMaterial(request):
    form = AddMaterialForm()
    if request.method == 'POST':
        form = AddMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material added Successfully!')
            return redirect('material-manage')

    context = {'form': form}
    return render(request, 'Trequest/AddMaterialForm.html', context)


@login_required(login_url='login')
def material_management(request):
    material = Material.objects.all()
    myfilter = MaterialFilter(request.GET, queryset=material)
    material = myfilter.qs
    context = {'material': material, 'myfilter': myfilter}
    return render(request, 'Trequest/material_management.html', context)
