from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from .models import UserProfile
from bootstrap_datepicker_plus.widgets import DatePickerInput

# Validator for names: only letters
name_validator = RegexValidator(
    regex=r'^[A-Za-z]+$',
    message='Only English alphabetic characters are allowed.'
)

class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=15,
        label="First Name",
        required=True,
        validators=[name_validator],
        help_text='Please enter English alphabetic characters only.',
        error_messages={'required': 'Required first name'},
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name here ..',
            'class': 'form-control'
        })
    )

    last_name = forms.CharField(
        max_length=15,
        label="Last Name",
        required=True,
        validators=[name_validator],
        help_text='Please enter English alphabetic characters only.',
        error_messages={'required': 'Required last name'},
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name here ..',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        max_length=255,
        label="Email",
        required=True,
        validators=[EmailValidator(message="Enter a valid email address.")],
        error_messages={'required': 'Required email'},
        widget=forms.TextInput(attrs={
            'placeholder': 'Email here ..',
            'class': 'form-control'
        })
    )

    password1 = forms.CharField(
        label='Password',
        min_length=8,
        required=True,
        help_text='Use 8 characters or more.',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label='Confirm Password',
        min_length=8,
        required=True,
        help_text='Re-enter the same password.',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password1') != cd.get('password2'):
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "password")
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            "password": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }


class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'cols': '20',
            'rows': '10',
            'placeholder': 'Write your bio here ..',
            'class': 'form-control',
        }),
        required=False
    )

    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text='Optional: Include country code (e.g., +1, +91)',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    address = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    city = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    state = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    country = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UserProfile
        fields = (
            'bio', 'profile_image', 'date_of_birth', 'gender',
            'phone_number', 'address', 'city', 'state', 'country'
        )
        widgets = {
            'date_of_birth': DatePickerInput(options={"format": "DD/MM/YYYY"}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
