from django.db import models

class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    caption = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.caption

class Intro(models.Model):
    text = models.TextField()

class Story(models.Model):
    text = models.TextField()

class Mission(models.Model):
    text = models.TextField()

class Vision(models.Model):
    text = models.TextField()

class Service(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    description = models.TextField()

class Stat(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

class CompanyProfile(models.Model):
    text = models.TextField()

class Copyright(models.Model):
    text = models.TextField()

class Navbar(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.title
