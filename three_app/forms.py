from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *




class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("A user with that username already exists.")
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email
    
    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    bio = forms.Textarea(attrs={'class': 'form-control'})
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.Textarea(attrs={'class': 'form-control'})

    class Meta:
        model = UserProfile
        fields = ('fname', 'lname', 'bio', 'email', 'birthdate', 'contact', 'gender', 'address')





class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'mobile_number', 'date', 'time', 'guest_count']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}),
            'date': forms.DateInput(attrs={'class': 'form-control datetimepicker-input', 'placeholder': 'Date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Time'}),
            'guest_count': forms.Select(attrs={'class': 'custom-select form-control text-dark'}),
        }





class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'number', 'email', 'amount',]                