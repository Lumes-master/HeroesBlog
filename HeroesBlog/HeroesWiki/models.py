from django.db import models
from django.urls import reverse


class Castle(models.Model):
    title = models.CharField(max_length=255, verbose_name='вид замка')
    slug = models.SlugField(unique=True)
    picture = models.FileField(upload_to="images")
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Замок - {self.title}'

    def get_absolute_url(self):
        return reverse('castle', kwargs={'castle_slug':self.slug})


class Unit(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя юнита')
    slug = models.SlugField(unique=True)
    picture = models.FileField(blank=True, upload_to="images")
    description = models.TextField(blank=True)
    castle = models.ForeignKey(Castle, related_name='castle', on_delete=models.CASCADE)

    def __str__(self):
        return f'Юнит - {self.title}'

    def get_absolute_url(self):
        return reverse('unit', args=[self.slug])


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    text = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to='images')
    date_created = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[self.pk])
