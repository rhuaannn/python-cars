from django import forms
from cars.models import Car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('Value', "Valor minimo tem que ser maior que 20.000")
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('value')
        if factory_year <  1999:
            self.add_error('factory_year', " Ano não permitido!")
            
        return factory_year