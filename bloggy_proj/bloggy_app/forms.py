from .models import Event, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.forms import AuthenticationForm


class EventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Event
        fields = '__all__'


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail:', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)
    first_name = forms.CharField(label='Имя:', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(label='Фамилия:', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Profile
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar')


class EventCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    slug = forms.SlugField(label='', widget=forms.TextInput(attrs={'hidden': True}))

    class Meta:
        model = Event
        exclude = ('views', 'datetime_of_create')

