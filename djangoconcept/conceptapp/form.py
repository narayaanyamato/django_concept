from django import forms
from conceptapp.models import Employee

class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields = ('name', 'empid', 'cname', 'cdesg', 'salary', 'pic')  
        widgets = {  
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),  
        'empid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Employee ID'}),  
        'cname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Name'}),  
        'cdesg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Designation'}),  
        'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Salary'}),  
        'pic': forms.FileInput(attrs={'class': 'form-control-file'}),  
      }

    
class Productform(forms.Form):

    pname=forms.CharField(widget=forms.TextInput(attrs={"placeholder":'Enter product name?',
                                                        "class":'form-control'}))
    price=forms.FloatField(widget=forms.TextInput(attrs={"placeholder":'Enter product price?',
                                                         "class":'form-control'}))
    pqty=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":'Enter product Quantity?',
                                                          "class":'form-control'}))
    desc=forms.CharField(widget=forms.TextInput(attrs={"placeholder":'Enter product Description?',
                                                       "class":'form-control'}))
    review=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":'Enter product Review?',
                                                            "class":'form-control'}))
    
    def clean_pname(self):
        print("product form validating")
        pname=self.cleaned_data['pname']
        if(len(pname)<3):
            raise forms.ValidationError("erroor in name")
        return pname

class customer(forms.Form):
    cname=forms.CharField(widget=forms.TextInput(attrs={"placeholder":'Enter User name?',
                                                        "class":'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={"placeholder":'Enter user Email name?',
                                                        "class":'form-control'}))
    phone=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":'Enter phone number ?',"class":'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={"placeholder":'Enter Address ?',"class":'form-control'}))
 

from django.contrib.auth.models import User

class Signup(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widget={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter first name"})
        }

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class Search(forms.Form):
      query = forms.CharField(label='Search', max_length=100)
    