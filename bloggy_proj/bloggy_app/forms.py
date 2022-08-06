from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class EventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Event
        fields = '__all__'


class RegisterUserFrom(UserCreationForm):
    username = forms.CharField(label='Логин:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail:', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)
    first_name = forms.CharField(label='Имя:', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(label='Фамилия:', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)


class EventCreateForm(forms.ModelForm):
    # title = forms.CharField(label='Название:', widget=forms.TextInput(attrs={: 'autoinput()'}))
    description = forms.CharField(widget=CKEditorUploadingWidget())
    url = forms.CharField(label='')

    class Meta:
        model = Event
        exclude = ('views', 'datetime_of_create')

