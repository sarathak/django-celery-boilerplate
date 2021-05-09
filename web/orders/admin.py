from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'products', 'price', 'created')
    date_hierarchy = 'created'
    search_fields = ('order_number',)


admin.site.register(Order, OrderAdmin)
