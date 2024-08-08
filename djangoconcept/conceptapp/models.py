from django.db import models
from django.urls import reverse

class Employee(models.Model):
    name=models.CharField(max_length=60)
    empid=models.CharField(max_length=40)
    cname=models.CharField(max_length=60)
    cdesg=models.CharField(max_length=70)
    salary=models.FloatField()
    pic=models.ImageField(upload_to="static/upload/")
    
class Student(models.Model):
    stdno=models.IntegerField()
    sname=models.CharField(max_length=40)
    college=models.CharField(max_length=40)
    Eductn=models.CharField(max_length=40)
    mark=models.FloatField()
    img=models.ImageField(upload_to='static/profile')

    def get_absolute_url(self):
        return reverse('cbvrec', kwargs={'pk': self.pk})
    def get_absolute_url(self):
        return reverse('cbvrec', kwargs={'pk': self.pk})

class Product(models.Model):
    pname=models.CharField(max_length=70)
    price=models.FloatField()
    pqty=models.IntegerField()
    desc=models.CharField(max_length=75)
    review=models.IntegerField()

class Customer(models.Model):   
    cname=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=80)

class Ormdata(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    job=models.CharField(max_length=50)
    salary=models.FloatField()
    address=models.CharField(max_length=80)


        
    
    