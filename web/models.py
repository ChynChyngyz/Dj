from django.db import models


class Image(models.Model):
    objects = None
    identifier = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.identifier


class Navigation(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField(default='')

    def __str__(self):
        return self.identifier


class TextBlock(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField(default='')

    def __str__(self):
        return self.identifier


class Promotion(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField(default='')

    def __str__(self):
        return self.identifier


class Carousel(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField(default='')

    def __str__(self):
        return self.identifier


class Case(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField(default='')

    def __str__(self):
        return self.identifier
