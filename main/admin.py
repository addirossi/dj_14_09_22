from django.contrib import admin

from .models import Product, Order, OrderPositions


class PositionsInline(admin.TabularInline):
    model = OrderPositions


class OrderAdmin(admin.ModelAdmin):
    inlines = [PositionsInline]


admin.site.register(Product)
admin.site.register(Order, OrderAdmin)

