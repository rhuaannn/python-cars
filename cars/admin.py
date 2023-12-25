from django.contrib import admin
from cars.models import Car, Brand, CarInventory
 
class CarAdmin(admin.ModelAdmin):
    # list display é a colunas da tabela car que vai ser criada no painel admim.
    # search significa os campos no qual ele vai pesquisar determinado item
    list_display = ('model', 'brand','factory_year', 'model_year', 'value')
    search_fields = ('model','brand__name')
    
    
class BrandAdmin(admin.ModelAdmin):
   list_display = ('name',)
   search_fields = ('name',)
   
class CarInventoryAdmin(admin.ModelAdmin):
    list_display= ('cars_count', 'cars_value', 'created_at')
    search_fields = ('model', 'cars__count')    
    
    
admin.site.register(Car,CarAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(CarInventory, CarInventoryAdmin)
