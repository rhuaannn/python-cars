from django import forms
from cars.models import Car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value < 1:
            self.add_error('Value', "Valor minimo tem que ser maior que 1")
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')

        if factory_year is not None and factory_year < 1999:
              self.add_error('factory_year', "Ano não permitido!")

        return factory_year
