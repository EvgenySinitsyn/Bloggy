from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date, datetime


class Profile(AbstractUser):
    avatar = models.ImageField('Аватар', upload_to='avatars', blank=True)


class Event(models.Model):
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='posters')
    date_of_event = models.DateField("Дата события", default=date.today)
    categories = models.ManyToManyField('Category', related_name='events', )
    slug = models.SlugField("slug", max_length=160, unique=True)
    datetime_of_create=models.DateTimeField('Время создания', default=datetime.now)
    draft = models.BooleanField("Черновик", default=True)
    views = models.IntegerField(default=0)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class EventPhotos(models.Model):
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    photo = models.ImageField('Фото', upload_to='event_photos')
    event = models.ForeignKey(Event, verbose_name='event', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Category(models.Model):
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    slug = models.SlugField("slug", max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'