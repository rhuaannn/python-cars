from django.db.models.signals import  post_save, post_delete
from django.dispatch import receiver
from django.forms import FloatField
from cars.models import Car, CarInventory


from django.db.models import Sum, Value
from django.db.models.functions import Coalesce

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Coalesce(Sum('value', output_field=FloatField()), Value(0))
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
