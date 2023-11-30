from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request):
 #usamos o __ para percorrer uma tabela para outra.
 #usando o contains do django, funcao pronta, vai trazer o elemento digitado
 #   cars = Car.objects.filter(brand__name = 'Fiat')
    cars = Car.objects.all()
    search = request.GET.get('search')
   
    if search:
         cars = Car.objects.filter(model__icontains=search)
         
    return render(
        request, 
        'cars.html',
        {'cars': cars}      
    )
     
        
def new_car_view(request):
    
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        print(new_car_form.data)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )