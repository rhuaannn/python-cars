from django.contrib import admin
from cars.models import Car, Brand
 
class CarAdmin(admin.ModelAdmin):
    # list display é a colunas da tabela car que vai ser criada no painel admim.
    # search significa os campos no qual ele vai pesquisar determinado item
    list_display = ('model', 'brand','factory_year', 'model_year', 'value')
    search_fields = ('model','brand__name')
    
    
class BrandAdmin(admin.ModelAdmin):
   list_display = ('name',)
   search_fields = ('name',)
    
admin.site.register(Car,CarAdmin)
admin.site.register(Brand,BrandAdmin)
