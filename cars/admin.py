from django.contrib import admin
from cars.models import Car, Brand, CarInventory


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')
    
class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('cars_count', 'cars_value')
    search_fields = ('cars_count', 'cars_value')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarInventory, CarInventoryAdmin)