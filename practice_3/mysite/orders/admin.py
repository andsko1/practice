from django.contrib import admin
from orders.models import Order
from orders.models import Customer

class OrderAdmin(admin.ModelAdmin):
    #list_display = ('itemid', 'created')
    #date_hierarchy = 'created'
    pass
class CustomerAdmin(admin.ModelAdmin):
    #list_display = ('firstName', 'lastName', 'address', 'email')
    pass
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
