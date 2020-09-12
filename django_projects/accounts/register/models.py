from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings

from django.db.models.signals import post_save
from register.utils import unique_order_id_generator
from django.db.models.signals import pre_save

ACCOUNT_CHOICES = (
    ('Savings', 'Savings'),
    ('Current', 'Current'),
    )

CURRENCY_CHOICES = (
    ('Rupee', 'Rupee'),
    ('US Dollar', 'US Dollar'),
    ('Euro', 'Euro'),
    ('Pound', 'Pound'),
    )

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50, null=True, blank=True)
    LastName = models.CharField(max_length=50)

    Address1 = models.TextField(max_length=100)
    Address2 = models.TextField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    PinCode = models.IntegerField()

    DOB = models.DateField()
    ContactNumber = models.IntegerField()
    Occupation = models.CharField(max_length=50)
    docImage = models.FileField(upload_to='register/pictures')

    def __str__(self):
        return self.FirstName

class Account(models.Model):
    AccountType = models.CharField(max_length=50, choices=ACCOUNT_CHOICES)
    Currency = models.CharField(max_length=50, choices=CURRENCY_CHOICES)
    AccountNumber = models.CharField(max_length=120)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.AccountNumber:
        instance.AccountNumber = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Account)