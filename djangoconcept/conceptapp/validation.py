from django import forms
   
class Validation(forms.Form):
    name=forms.CharField(max_length = 50,widget=forms.TextInput(attrs={
        "placeholder":"Enter user name","class":"form-control"
    }))
    email=forms.EmailField(widget=forms.TextInput(attrs={
         "placeholder":"Enter Email name","class":"form-control"
    }))
    phone=forms.CharField(widget=forms.TextInput(attrs={
         "placeholder":"Enter phone number ","class":"form-control"
    }))
    address=forms.CharField( max_length=120,widget=forms.Textarea(attrs={
         "placeholder":"Enter your Address ","class":"form-control"
    }))
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={
          "placeholder":"Enter password ","class":"form-control"
    }))
    confirm_password = forms.CharField(label='Confirm Password', 
    widget=forms.PasswordInput(attrs={
          'placeholder': 'Confirm your password','class':'form-control'}))
    
    date_of_birth = forms.DateField(label='Date of Birth',
    widget=forms.DateInput(attrs={'placeholder': 'Enter your date of birth','class':'form-control'}))

    gender=forms.CharField(max_length=13,widget=forms.RadioSelect(choices=(("male","male"),("female","female")))) 
    
    favorite_color = forms.ChoiceField(label='Favorite Color', choices=[('0','------select --------'),('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')], widget=forms.Select(attrs={"class":"form-select"}))
    
    hobbies = forms.MultipleChoiceField( label='Hobbies', choices=[('reading', 'Reading'), ('writing', 'Writing'), ('coding', 'Coding')], widget=forms.CheckboxSelectMultiple() )
    
    marital_status = forms.ChoiceField(label='Marital Status', choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')], widget=forms.RadioSelect())
    
    def clean_name(self):
        print("validate name")
        name=self.cleaned_data['name']
        if(len(name)<3):
            raise forms.ValidationError("user name cant be less than 3 char")
    
        return name
    
    
    def clean_email(self):
        import re
        print("email validatig")
        email=self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):

            raise forms.ValidationError("Invalid email address")
        return email
    
    def clean_phone(self):
        print("validate phone number")
        phone=self.cleaned_data['phone'] 
        if(len(phone)!=10):
            raise forms.ValidationError("number length sould 10")
    
    def clean_address(self):
        print("validating address field")
        address=self.cleaned_data['address']
        if(len(address)<12):
            raise forms.ValidationError("address should be be grater 12 char")
        return address
    
    def clean_password(self):
        print("password validating")
        passd=self.cleaned_data['password']
        if(len(passd)<5):
            raise forms.ValidationError("pass should 5char")
 
        
        return passd        
    
    


