from django.urls import path
from . import views
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('new_event/', views.EventCreateView.as_view(), name='new_event'),
    path('validate_url/', views.validate_url, name='validate_url'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('<slug:slug>/', views.EventDetailView.as_view(), name='detail'),
]


if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()