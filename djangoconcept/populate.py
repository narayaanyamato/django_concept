
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoconcept.settings')
import django
django.setup()
from random import*
from faker import Faker
fobj=Faker()
from conceptapp.models import Ormdata
def fakedatagen(n):
    for i in range(n):
        fname=fobj.name()
        femail=fobj.email()
        fphone = fobj.random_int(min=7847869140, max=9439325600, step=100)
        fjob=fobj.job()
        fsalary=randint(10000,20000)
        faddress=fobj.city()
        emp=Ormdata.objects.get_or_create(name=fname,phone=fphone,email=femail,
        job=fjob,salary=fsalary,address=faddress)

n=int(input("Enter number of record  :"))
fakedatagen(n)
print("rec inserted is ",n)        