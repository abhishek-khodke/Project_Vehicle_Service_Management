from django.contrib import admin
from .models import Customer, Vehicle, ServiceRecord

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(ServiceRecord)
