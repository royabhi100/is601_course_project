
# Register your models here.
from django.contrib import admin

from .models import DataSetDesc, Order, Trade

admin.site.register(DataSetDesc)
admin.site.register(Order)
admin.site.register(Trade)