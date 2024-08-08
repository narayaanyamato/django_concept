from django.contrib import admin
from conceptapp.models import Employee,Student,Product,Customer,Ormdata

class EmploeeAdmin(admin.ModelAdmin):
    list_display=['name','empid','cname','cdesg','salary','pic']

class StudentAdmin(admin.ModelAdmin):
    list_display=['stdno','sname','college','Eductn','mark','img'] 

class ProductAdmin(admin.ModelAdmin):
    list_display=['pname','price','pqty','desc','review']  

class CustomerAdmin(admin.ModelAdmin):
     list_display=['cname','phone','email','address'] 

class OramdataAdmin(admin.ModelAdmin):
    list_display=['name','phone','email','job','salary','address']


admin.site.register(Employee,EmploeeAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Ormdata,OramdataAdmin)