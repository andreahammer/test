from django.contrib import admin
from .models import Car
from .models import Customer

from .models import Employee
from .customer import Customer
from .employee import Employee



admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Employee)