from django.db import models

# Create your models here.
class Table1(models.Model):
    state=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    name=models.TextField()
    category=models.CharField(max_length=30)
    image=models.URLField()
    desc=models.TextField()
    byair=models.TextField()
    bytrain=models.TextField()
    byroad=models.TextField()

class Category(models.Model):
    name=models.CharField(max_length=20)
    img=models.URLField()
    
    
class State(models.Model):
    name=models.CharField(max_length=20)
    img=models.URLField()
    
class Pay(models.Model):
    From=models.CharField(max_length=30)
    to=models.TextField()
    prize=models.IntegerField()
    
class Slide(models.Model):
    name=models.CharField(max_length=30)
    image=models.URLField()
    
class Contact(models.Model):
    name=models.CharField(max_length=60)
    mobile_no=models.BigIntegerField()
    email=models.CharField(max_length=60)
    review=models.TextField()
    
class payment(models.Model):
    From=models.CharField(max_length=60)
    To=models.CharField(max_length=60)
    By_Train=models.IntegerField()
    By_Road=models.IntegerField()
    By_Air=models.IntegerField()
    
class Details1(models.Model):
    name=models.CharField(max_length=60)
    mobile_no=models.BigIntegerField()
    email=models.CharField(max_length=60)
    gender=models.TextField()
    prize=models.IntegerField()
    mode=models.CharField(max_length=30)
    From=models.CharField(max_length=30)
    To=models.CharField(max_length=30)
    date=models.DateField()
    age=models.CharField(max_length=30)
    image=models.URLField()
    
    