from django.shortcuts import render,redirect
from django.db.models import Q
from django.db  import transaction
from django.contrib import messages
from django.core.validators import ProhibitNullCharactersValidator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from Trequest.decorators import allowed_users
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
@allowed_users(allowed_roles=['StoreManager'])
def deletematerial(request, pk):
    material = get_object_or_404(Material, id=pk)
    material.delete()
    messages.success(request, 'Material deleted Successfully!')
    return redirect('material-manage')
    # term = Material.objects.get(id=pk)
    # if request.method == 'POST':
    #     term.delete()
    #     return redirect('material-manage')
    # context = {'term': term}
    # return render(request, 'MaterialApp/delete_material.html', context)
def delete_request(request, pk):
    material = get_object_or_404(MaterialRequest, id=pk)
    material.delete()
    messages.success(request, 'Material deleted Successfully!')
    return redirect('view_material_request')    

@login_required(login_url='login')
@allowed_users(allowed_roles=['StoreManager'])
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
    return render(request, 'MaterialApp/add_material_form.html', context)

@login_required(login_url='login')
def view_material_request(request):
    materialView=MaterialRequest.objects.filter(status="Pending")
    context = {'materialView': materialView}
    return render(request, 'MaterialApp/view_material_request.html', context)

def view_request(request):
    materialView=MaterialRequest.objects.filter(user=request.user)
    context = {'materialView': materialView}
    return render(request, 'MaterialApp/view_request.html', context)

#for aprove they material with 
@login_required(login_url='login')
@transaction.atomic    
def material_detail(request, id):
    material_detail = MaterialRequest.objects.get(id=id)
    
    
    #form = ApprovedMaterial(instance=material_detail)    
    if request.method == 'POST':
        #form = ApprovedMaterial(request.POST, instance=material_detail)
        #if form.is_valid():
        with transaction.atomic():
            Materil_check= Material.objects.get(name = material_detail.new_material_name)
            if (Materil_check.quantity >= material_detail.quantity_of_new):

        
                q = material_detail.quantity_of_new

                
                Materil_check.quantity -= q
                Materil_check.save()
                material_detail.status = "approved"
                material_detail.save()
                messages.success(request,"Approved Successfully")
                return redirect('view_material_request')

                
            else:
                messages.warning(request,"Amount of material your requested not available")
                return redirect('view_material_request')
                             

    context = {'material_detail': material_detail}
    return render(request, 'MaterialApp/material_detail.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['StoreManager','Admin'])
def AddMaterial(request):
    form = AddMaterialForm()
    if request.method == 'POST':
        form = AddMaterialForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request, 'Material added Successfully!')
            return redirect('material-manage')

    context = {'form': form}
    return render(request, 'MaterialApp/add_material_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['StoreManager'])
def material_management(request):
    material = Material.objects.all()
    query = request.GET.get('search')
    if query:
        material = Material.objects.filter(Q(name__icontains=query) |
                                    Q(type_of__icontains=query))
    context = {'material': material}
    return render(request, 'MaterialApp/material_management.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Mechanic','StoreManager'])
def material_request(request):  
    if request.method == 'POST':
        form = MaterialRequestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Request sent successfully')
            return redirect('view_request')
        else:
            print("invalid data")
    else:
        form = MaterialRequestForm()
    context={'form': form}

    return render(request, 'MaterialApp/material_request.html', context)

def view_alert(request):
    alert = Material.objects.filter(quantity__lte=10)
    alert1 = Material.objects.filter(quantity__lte=10).count()


    context={'alert': alert, 'alert1':alert1}

    return render(request, 'MaterialApp/alert.html', context)

def alert_count():
  return Material.objects.filter(quantity__lte=10).count()
      