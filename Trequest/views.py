from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from  django.contrib.auth.forms import PasswordChangeForm
from Trequest.forms import *
from django.core.mail import send_mail
from .filters import MaterialFilter, UserFilter
import random
import string
from django.http.response import JsonResponse

# registered users can login in to the system
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

# creating account for the users
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

# AJAX
def load_department(request):
    school_id = request.GET.get('school_id')
    departments = Department.objects.filter(school_id=school_id).order_by('name')
    context={'departments':departments}
    return render(request, 'Trequest/department_dropdown_list_options.html', context)
    # print(list(departments.values('id','name')))
    # return JsonResponse(list(departments.values('id', 'name')), safe=False)

#editing/updating user account 
def edit_account(request):
    if request.method == 'POST':
        a_form = UserAccountEditForm(request.POST, instance=request.user)
        p_form=UserProfileEditForm(request.POST,instance=request.user.passenger)
        if a_form.is_valid() and p_form.is_valid():
            a_form.save()
            p_form.save()
            messages.success(request, 'Profile updated Successfully!')
            return redirect('profile')

    else:
        a_form = UserAccountEditForm(instance=request.user)
        p_form=UserProfileEditForm(instance=request.user.passenger)

    context = {'a_form': a_form,'p_form':p_form}
    return render(request, 'Trequest/edit_account.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Password Changed successfully')
            return redirect('change-password')
    else:
        form=PasswordChangeForm(request.user)
    context={'form':form}
    return render(request,'Trequest/change_password.html',context)


@login_required(login_url='login')
def index(request):
    schedule = Schedule.objects.all().order_by('-date')
    total_user = MyUser.objects.all()
    tsho_pending_request = TransportRequest.objects.filter(status='Pending', status2='Approved', status3='Approved')
    dep_pending_request = TransportRequest.objects.filter(status2='Pending',
                            passenger__department=request.user.department).exclude(passenger__role="DepartmentHead")
    sch_pending_request = TransportRequest.objects.filter(status3='Pending', status2='Approved',
                                passenger__school=request.user.school).exclude(passenger__role="SchoolDean")
    app = total_user.count()
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
               'sch_pend': sch_pend,
               
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


 #  vehicle related
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
            return redirect('vehicle-manage')
    else:
        form = VehicleRegisterForm()
    context = {'form': form}
    return render(request, 'Trequest/register_vehicle.html', context)

def edit_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method == 'POST':
        form = VehicleRegisterForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle updated Successfully!')
            return redirect('vehicle-manage')

    else:
        form = VehicleRegisterForm(instance=vehicle)

    context = {'form': form}
    return render(request, 'Trequest/update_vehicle.html', context)

@login_required(login_url='login')
def repaired_vehicle(request):
    return render(request,'Trequest/repaired_vehicle.html')

@login_required(login_url='login')
def material_management(request):
    return render(request, 'Trequest/material_management.html')


@login_required(login_url='login')
@login_required(login_url='login')
def profile(request):
    return render(request, 'Trequest/profile.html')



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
            #user =TransportRequest.objects.get(passenger=request.user)
            role= MyUser.objects.get(username=request.user).role
           

            if role == 'DepartmentHead':
               
                #TransportRequest.objects.create(status2="Approved")
                #status2 = TransportRequest.objects.get(status2="Approved")
                s2 = TransportRequest.objects.filter(passenger=request.user)[0:1]
                TransportRequest.objects.filter(id__in=s2).update(status2 = "Approved")
                # status2=s2.status2
            if role == 'SchoolDean':
                s2 = TransportRequest.objects.filter(passenger=request.user)[0:1]
                TransportRequest.objects.filter(id__in=s2).update(status2 = "Approved",status3="Approved")
                
                # status2.save()
            messages.success(request, 'Request sent Successfully!')
            return redirect('my-request')
    else:
        form = MakeRequestForm()
    context = {'form': form}
    return render(request, 'Trequest/make_request.html', context)




# @login_required(login_url='login')
# def tsho_assign_request(request, id):
#     app = TransportRequest.objects.get(id=id)
#     if request.method == 'POST':
#         request_form = ApproveRequestForm(request.POST)
#         if request_form.is_valid():
#             obj = request_form.save(commit=False)
#             obj.user = app
#             obj.save()
#             return send_email(request)
#             messages.success(request, 'Request Approve Successfully!')
#             return redirect('tsho-view-approved-request')
#     else:
#         request_form = ApproveRequestForm()
#     context = {'form': request_form, 'app': app}
#     return render(request, 'Trequest/assign_approved_request.html', context)


def department_view_request(request):
    transport1 = TransportRequest.objects.filter(status2='Pending')
    # exclude the request sent from department to not visible to them selves
    transport=transport1.exclude(passenger__role = "DepartmentHead").order_by('-created_at') 
    context = {'transport': transport}
    return render(request, 'Trequest/department_view_request.html', context)


def department_view_approved_request(request):
    transport = TransportRequest.objects.filter(status2='Approved').order_by('-created_at')
    context = {'transport': transport}
    return render(request, 'Trequest/department_view_approved_request.html', context)


def school_view_request(request):
    transport1 = TransportRequest.objects.filter(status2='Approved', status3='Pending')
    # exclude the request sent from school to not visible to them selves
    transport=transport1.exclude(passenger__role = "SchoolDean").order_by('-created_at') 
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
            messages.success(request, 'Request approved Successfully!')
            return redirect('department-view-approved-request')
    else:
        form = DepartmentApproveForm(instance=approve)
    context = {'form': form, 'approve': approve}
    return render(request, 'Trequest/department_approve_request.html', context)



def tsho_approve_request(request, id):
    vehicle=Vehicle.objects.filter(currently='Inside',status='Occupied')
    approve = get_object_or_404(TransportRequest, id=id)
    if request.method == 'POST':
        form = TshoApproveForm(request.POST, instance=approve)
        if form.is_valid():
            form.save()
            # for sending email to respective user
            subject = request.POST.get('subject')
            date = request.POST.get('message')
            time=request.POST.get('message2')
            new_driver=request.POST.get('driver')
            driver_fname=MyUser.objects.get(username=new_driver).first_name
            driver_lname=MyUser.objects.get(username=new_driver).last_name
            driver_full_name=driver_fname + " "+ driver_lname
            driver_phone=MyUser.objects.get(username=new_driver).phone
            vehicle_plate=Vehicle.objects.get(driver__user__username=new_driver).plate_number
            message="Your driver name: "+  driver_full_name + "\n" + "Driver phone number: " + driver_phone + "\n "+ "Date of your trip: " + date + "\n "+ "Time of your trip: " + time + "\n "+ "Your vehicle plate number: " + vehicle_plate
            email = request.POST.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [email], fail_silently=False)
            return render(request, 'Trequest/email_sent.html', {'email': email})
    else:
        form = TshoApproveForm(instance=approve)
    context = {'form': form,
                'approve': approve,
                'vehicle':vehicle
              }
    return render(request, 'Trequest/tsho_approve_request.html', context)

def school_approve_request(request, id):
    approve = get_object_or_404(TransportRequest, id=id)
    if request.method == 'POST':
        form = SchoolApproveForm(request.POST, instance=approve)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request approved Successfully!')
            return redirect('school-view-approved-request')
    else:
        form = SchoolApproveForm(instance=approve)
    context = {'form': form, 'approve': approve}
    return render(request, 'Trequest/school_approve_request.html', context)


@login_required(login_url='login')
def my_request(request):
    myrequest = TransportRequest.objects.filter(passenger=request.user).order_by("-created_at")
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

# def notifications(request):
   
#     notifications=Notifications.objects.filter(is_viewed = False)
#     not_count=notifications.count()
#     context={'notifications':notifications,'not_count':not_count}
#     return render(request, 'Trequest/notifications.html', context)
    
def material_request(request):
    form = MaterialRequestForm()
    if request.method == 'POST':
        form = MaterialRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request sent successfully')

<<<<<<< HEAD
    return render(request, 'Trequest/MaterialRequest.html')
# Driver Evaluation View
@login_required(login_url='login')
def evaluate(request):
    if request.method == 'POST':
        form = EvaluateDriverForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.duser = request.user
            form.save()
            messages.success(request, 'Rated Successfully!')
            return redirect('index')
    else:
        form = EvaluateDriverForm()
    context = {'form': form}
    return render(request, 'Trequest/evaluate_driver.html', context)
=======
    context = {'form': form}
    return render(request, 'Trequest/material_request.html', context)
>>>>>>> e378ad9e8501ca84f5651b003982ea4f7542152f
