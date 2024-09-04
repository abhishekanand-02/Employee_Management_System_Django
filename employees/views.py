from django.shortcuts import render, redirect, get_object_or_404
from .models import Name
from django.contrib import messages

def home(request):
    return render(request, 'employees/index.html')

def create_name(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        first_name = request.POST['first_name']
        role=request.POST['role']
        last_name = request.POST['last_name']
        emergency_contact = request.POST['emergency_contact']
        hire_date = request.POST['hire_date']
       
        is_currently_working = request.POST.get('is_currently_working', 'off') == 'on'

        Name.objects.create(
            role=role,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            emergency_contact=emergency_contact,
            hire_date=hire_date,
            is_currently_working=is_currently_working
        )
        
        messages.success(request, 'Employee created successfully.')
        return redirect('read_names')
    
    return render(request, 'employees/create.html')

def read_names(request):
    names = Name.objects.all()
    return render(request, 'employees/read_names.html', {'names': names})

def update_name(request, id):
    name = get_object_or_404(Name, id=id)
    
    if request.method == 'POST':
        name.role=request.POST['role']
        name.employee_id = request.POST['employee_id']
        name.first_name = request.POST['first_name']
        name.last_name = request.POST['last_name']
        name.emergency_contact = request.POST['emergency_contact']
        name.hire_date = request.POST['hire_date']
        name.is_currently_working = request.POST.get('is_currently_working', 'off') == 'on'
        name.save()
        
        messages.success(request, 'Employee updated successfully.')
        return redirect('read_names')
    
    return render(request, 'employees/update.html', {'name': name})

def delete_name(request, id):
    name = get_object_or_404(Name, id=id)
    
    if request.method == 'POST':
        name.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('read_names')
    
    return render(request, 'employees/delete.html', {'name': name})