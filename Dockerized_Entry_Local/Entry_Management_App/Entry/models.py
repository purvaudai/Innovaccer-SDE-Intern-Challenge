from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class host(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

class visitor(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=False)
    #phone=even_field = models.IntegerField(validators=[validate_phone])

class visit(models.Model):
    #id=models.AutoField(primary_key=True)
    timeofadding=models.DateTimeField(auto_now_add=True)
    timein=models.DateTimeField()
    timeout=models.DateTimeField(null=True)
    tenttimeout=models.DateTimeField(null=True)
    visitor=models.ForeignKey(visitor, related_name='visitor', on_delete=models.CASCADE)
    host=models.ForeignKey(host, related_name='host', on_delete=models.CASCADE)
    address=models.CharField(max_length=250)
'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        host.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.host.save()'''