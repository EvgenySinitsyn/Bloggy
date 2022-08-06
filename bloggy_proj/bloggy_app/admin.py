from django import forms
from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class EventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class': 'default'}))
    class Meta:
        model = Event
        fields = '__all__'


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    prepopulated_fields = {"url": ("title", )}
    exclude = ('views',)


class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {"url": ("title", )}


admin.site.register(Event, EventAdmin)
admin.site.register(EventPhotos)
admin.site.register(Category, CategoryAdmin)

