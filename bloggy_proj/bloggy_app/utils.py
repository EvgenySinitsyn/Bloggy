from .models import *


class DataMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = self.request.GET.get('cat', '')
        if category == '':
            context['events'] = Event.objects.filter(draft=False).order_by('-date_of_event', '-id')
        else:
            context['events'] = Event.objects.filter(draft=False, categories__url=category).order_by('-date_of_event', '-id')
            context['cat'] = Category.objects.get(url=category).title
        context['popular_events'] = Event.objects.all().order_by('-views')[:3]
        context['categories'] = Category.objects.all().order_by('title')

        return context