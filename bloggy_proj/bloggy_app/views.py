from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect

from .utils import DataMixin
from django.urls import reverse_lazy

from .forms import RegisterUserForm, EventCreateForm, LoginUserForm

from .models import *
from django.views.generic import DetailView, CreateView, TemplateView


class HomeView(DataMixin, TemplateView):
    template_name = 'bloggy_app/index.html'


class EventDetailView(DataMixin, DetailView):

    model = Event
    template_name = 'bloggy_app/single.html'
    slug_field = ('slug')
    context_object_name = 'event'


class RegisterUserView(DataMixin, CreateView):
    model = Profile
    form_class = RegisterUserForm
    template_name = 'bloggy_app/register.html'
    success_url = reverse_lazy('home')


class EventCreateView(DataMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'bloggy_app/new_event.html'
    success_url = reverse_lazy('home')



class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'bloggy_app/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

def validate_slug(request):
    slug = request.GET.get('slug')
    response = {'is_taken': Event.objects.filter(slug__iexact=slug).exists()}
    return JsonResponse(response)


