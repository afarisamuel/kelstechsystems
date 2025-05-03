from django.contrib.auth.models import User
from django.db import models


class HomeCarousel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return self.title



class ChooseUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title


class Testimonials(models.Model):

    clientName = models.CharField(max_length=100)
    clientProfession = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.clientName


class Team(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField()
    def __str__(self):
        return self.name


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Service, on_delete=models.CASCADE)
    subTitle = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title.title


class ContactUs(models.Model):
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject


class SocialLink(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    def __str__(self):
        return self.title



class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.name
