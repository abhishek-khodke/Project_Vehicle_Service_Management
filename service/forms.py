# service/forms.py

from django import forms
from .models import Customer, Vehicle, ServiceRecord

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['customer', 'make', 'model', 'year']

class ServiceRecordForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = ['vehicle', 'service_date', 'description', 'cost']
