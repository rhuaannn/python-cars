from django.db.models.signals import pre_save, pre_delete, pre_init,post_delete,post_save
from django.dispatch import receiver

from cars.models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('## PRE ##')
    

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('## POST ##')
    
    
@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print('## PRE ##')
    

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('## POST ##')
    print('##', instance)