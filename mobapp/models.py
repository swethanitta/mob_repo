from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    uname = models.CharField(max_length = 50, null = True, blank = True, default = None)
    email = models.EmailField(max_length = 50, null = True, blank = True, default = None)
    phno = models.IntegerField(max_length=12, null = True, blank = True, default = None)
    add = models.TextField(max_length=50, null = True, blank = True, default = None)
    
@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        
@receiver(post_save, sender = User)        
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
        
class product(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
          return self.name

class Brands(models.Model):
    bname = models.CharField(max_length = 50)
    def __str__(self):
          return self.bname

class pro_brand_map(models.Model):
    pid = models.ForeignKey('product')
    bid = models.ForeignKey('Brands')

class Pro_models(models.Model):
    mapid = models.ForeignKey('pro_brand_map')
    mod_name = models.CharField(max_length = 50)
    display = models.FloatField()
    processor = models.FloatField()
    ram = models.FloatField()
    fcam = models.FloatField()
    batt_cap = models.FloatField()
    price = models.FloatField()
    image = models.ImageField()
    
class Rating(models.Model):
    uid = models.ForeignKey('Profile')
    pro_mod_id = models.ForeignKey('Pro_models')
    rate = models.FloatField()
     
class booking(models.Model):
    uid = models.ForeignKey('Profile')
    pro_mod_id = models.ForeignKey('Pro_models')      
    quantity = models.IntegerField()
      


      
    
