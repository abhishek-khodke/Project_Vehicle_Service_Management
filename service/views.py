# service/views.py

from django.shortcuts import render
from .models import Customer, Vehicle, ServiceRecord
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from .forms import CustomerForm
from .models import Vehicle
from .forms import VehicleForm
from .models import ServiceRecord
from .forms import ServiceRecordForm


def index(request):
    return render(request, 'service/index.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'service/customer_list.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'service/customer_form.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'service/customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'service/customer_confirm_delete.html', {'customer': customer})

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'service/vehicle_list.html', {'vehicles': vehicles})


def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'service/vehicle_form.html', {'form': form})

def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'service/vehicle_form.html', {'form': form})

def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'service/vehicle_confirm_delete.html', {'vehicle': vehicle})


def service_record_list(request):
    service_records = ServiceRecord.objects.all()
    return render(request, 'service/service_record_list.html', {'service_records': service_records})

def service_record_create(request):
    if request.method == 'POST':
        form = ServiceRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_record_list')  # Redirect to the list view after saving
    else:
        form = ServiceRecordForm()  # Create an empty form for GET requests
    return render(request, 'service/service_record_form.html', {'form': form})

def service_record_update(request, pk):
    service_record = get_object_or_404(ServiceRecord, pk=pk)
    if request.method == 'POST':
        form = ServiceRecordForm(request.POST, instance=service_record)
        if form.is_valid():
            form.save()
            return redirect('service_record_list')  # Redirect to the list view after saving
    else:
        form = ServiceRecordForm(instance=service_record)  # Populate form with existing record data
    return render(request, 'service/service_record_form.html', {'form': form})

def service_record_delete(request, pk):
    service_record = get_object_or_404(ServiceRecord, pk=pk)
    if request.method == 'POST':
        service_record.delete()
        return redirect('service_record_list')  # Redirect to the list view after deleting
    return render(request, 'service/service_record_confirm_delete.html', {'service_record': service_record})