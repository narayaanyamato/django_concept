from django.shortcuts import render
from conceptapp.form import Employeeform,Productform,customer
from conceptapp.models import Employee
from django.shortcuts import render,redirect
#for img del when rec delete
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request,'pages/index.html')

def fvb_rec_view(request):
    emp=Employee.objects.all()
    return render(request,'pages/fbv/recview.html',{"emprec":emp})

def fbv_add(request):
    emp= Employeeform()
    if request.method=='POST':
        emp= Employeeform(request.POST,request.FILES)
        if emp.is_valid():
            emp.save(commit=True)
            print("data summited")
            return redirect('/recview')

    return render(request,'pages/fbv/addemp.html',{"emp":emp})

@receiver(post_delete, sender=Employee)
def delete_associated_picture(sender, instance, *args, **kwargs):
    if instance.pic:
        instance.pic.delete(save=False)

def fbv_del(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/recview')

def fbv_update(request,id):
    emp=Employee.objects.get(id=id)
    emp_form= Employeeform(instance=emp)
    if request.method=='POST':
        emp_form= Employeeform(request.POST,instance=emp)
        if(emp_form.is_valid()):
            emp_form.save()
            print("data upated")
        return redirect('/recview')
    return render(request,'pages/fbv/updarerec.html',{"emp":emp_form})



from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from conceptapp.models import Student
from django.urls import reverse_lazy
class stdrec_view(ListView):
    model=Student
    template_name='pages/cbv/view_rec.html'
    context_object_name='rec_list'

class stdadd_view(CreateView):
    model=Student
    fields='__all__'
    template_name='pages/cbv/add_rec.html'

class stdDetail_view(DetailView):
    model = Student
    template_name = 'pages/cbv/detail_rec.html'
    context_object_name='rec'

class stdupdate_view(UpdateView):
    model = Student
    template_name = 'pages/cbv/update_rec.html'
    fields='__all__'

class stddel_view(DeleteView):
    model=Student
    fields='__all__'
    template_name='pages/cbv/del_rec.html' 
    success_url=reverse_lazy('recview') 
    
def product_view(request):
    p=Productform()
    if request.method=='POST':
        p=Productform(request.POST)
        if p.is_valid():
            print("submited form")
    return render(request,'pages/session/product.html',{"p":p})    

from conceptapp.form import customer      
def customer_view(request):
    
    if request.method=='POST':
        c=customer(request.POST)
        if c.is_valid():
            name=request.POST['pname']
            price=request.POST['price']
            qty=request.POST['pqty']
            desc=request.POST['desc']
            review=request.POST['review']
            request.session['product_n']=name
            request.session['product_price']=price
            request.session['product_pqty']=qty
            request.session['product_desc']=desc
            request.session['product_review']=review

    c=customer()
    return render(request,'pages/session/customer.html',{"c":c})

def preview(request):
     user_name=request.POST['cname']
     user_email=request.POST['email']
     user_phone=request.POST['phone']
     user_address=request.POST['address']

     pname=request.session['product_n']
     pprice=request.session['product_price']
     pqty=request.session['product_pqty']
     pdesc=request.session['product_desc']
     preview=request.session['product_review']

     if request.method=="POST":
         c=customer(request.POST)
         p=Productform(request.POST)
         if(c.is_valid() and p.is_valid()):
            c.save(commit=True)
            p.save(commit=True)
            print("data submited")

     return render(request,'pages/session/preview.html',{"user_name":user_name,
     "user_email":user_email,"user_phon":user_phone,"user_phone":user_phone,
      "user_address":user_address,"pname":pname,"pprice":pprice,"pqty":pqty,"pdesc":pdesc,"preview":preview})


from conceptapp.validation import Validation

@login_required
def Validation_view(request):
    v=Validation()
    if request.method=='POST':
        v=Validation(request.POST)
        if v.is_valid():
            print("submited successfully")
    return render(request,'pages/validation.html',{"v":v})

from conceptapp.form import Signup,LoginForm

def logup_view(request):
    s=Signup()
    if request.method=='POST':
        s=Signup(request.POST)
        if s.is_valid():
            request.session['name']=request.POST['first_name']
            user=s.save()
            user.set_password(user.password)
            user.save()
            print("data submited")
            return redirect('/login')
            
    return render(request,'pages/auth/login.html',{"s":s})


def profile_view(request):
    login_name=request.session['name']
    return render(request,'pages/auth/profile.html',{"name":login_name})

def login_view(request):
    
    if request.method=='POST':
        form=LoginForm(request.POST)
        user=request.POST['username']
        pasd=request.POST['password']
        user = authenticate(username=user, password=pasd)
        if user is not None:
            login(request,user)
            return redirect('/profile')
    form=LoginForm()    
    return render(request,'pages/auth/signup.html',{"form":form})


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('/')

from conceptapp.models import Ormdata,Product
from conceptapp.form import Search
from django.db.models import Q
def orm_view(request):
    #o=Ormdata.objects.all()
    #o=Ormdata.objects.filter(name__contains='sa')
    #o=Ormdata.objects.filter(name__startswith='N')
    #o=Ormdata.objects.filter(name__startswith='N')
    #o=Ormdata.objects.filter(salary__lt=50000)
    #o=Ormdata.objects.filter(salary__lt=32000)
    #o=Ormdata.objects.filter(salary__gt=3000)
    #o=Ormdata.objects.filter(email__contains='kyliesimon@example.co')
    #o=Ormdata.objects.filter(id__in=[56,78,90,43])
   # o=Ormdata.objects.filter(name__in=['Doris Thornton','Dennis Davis'])
   # o=Ormdata.objects.filter(salary__range=[10000,25000])
   # o=Ormdata.objects.filter(salary__gt=10000) | Ormdata.objects.filter(name__startswith='D')
    #o=Ormdata.objects.filter(salary__gt=20000) | Ormdata.objects.filter(name__startswith='D')
    #o=Ormdata.objects.filter(Q(salary__gt=19000) | Q(name__startswith='s'))
   # o=Ormdata.objects.filter(salary__lt=12000) & Ormdata.objects.filter(name__startswith='a')
    #o=Ormdata.objects.filter(Q(salary__gt=10000) & Q(name__startswith='c'))
    #o=Ormdata.objects.filter(salary__gt=10000, name__endswith='n')
    #o=Ormdata.objects.all().order_by('name')
    #o=Ormdata.objects.all().order_by('salary')
    #o=Ormdata.objects.filter(~Q(name__endswith='n'))
    #o=Ormdata.objects.exclude(Q(name__endswith='a'))
    o1=Ormdata.objects.filter(~Q(name__endswith='n'))
    o2=Ormdata.objects.filter(salary__gt=18000)
    o=o1.union(o2)
    return render(request,'pages/orm_view.html',{"o":o})

def result_view(request):
    s=Search()
    return render(request,'pages/res.html',{"s":s})    

def search_rec(request):
    if request.method=='POST':
        s=Search(request.POST)
        if s.is_valid():
            qry=s.cleaned_data['query']
            results = Ormdata.objects.filter(name__startswith='qry') 
            return redirect('/srec')
    return render(request,'pages/viewrec.htm',{"res":results})

def cookie_view(request):
    p=Productform()
    response=render(request,'pages/product_view.html',{"p":p})
    if request.method=='POST':
        p=Productform(request.POST)   
        if(p.is_valid()):
            pname=p.cleaned_data['pname']
            price=p.cleaned_data['price']
            pqtye=p.cleaned_data['pqty']
            pdesc=p.cleaned_data['desc']
            review=p.cleaned_data['review']
            response.set_cookie(pname,price,pqtye,pdesc,review)
    return response
        
def cart_view(request):
    return render(request,'pages/cart.html')

def filter_view(request):
    return render(request,'pages/filter.html')
