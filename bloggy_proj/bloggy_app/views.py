from django.http import JsonResponse
from django.views import View

from .utils import DataMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import RegisterUserFrom, EventCreateForm

from .models import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView


class HomeView(DataMixin, TemplateView):

    template_name = 'bloggy_app/index.html'


class EventDetailView(DataMixin, DetailView):

    model = Event
    template_name = 'bloggy_app/single.html'
    slug_field = ('url')
    context_object_name = 'event'


class RegisterUserView(DataMixin, CreateView):
    model = User
    form_class = RegisterUserFrom
    template_name = 'bloggy_app/register.html'
    success_url = reverse_lazy('home')


class EventCreateView(DataMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'bloggy_app/new_event.html'
    success_url = reverse_lazy('home')


def validate_url(request):
    url = request.GET.get('url', None)
    queryset = Event.objects.filter(url__iexact=url)
    response = {'url': queryset[0].url} if queryset else {'url': None}
    return JsonResponse(response)


