from django.contrib.auth.models import User
from django.db import models


SOCIAL_MEDIA = (("FB", "FACEBOOK"), ("IG", "INSTAGRAM"), ("X", "X(TWITTER)"), ("YT", "YOUTUBE"), ("LN", "LINKEDIN"))

class HomeCarousel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    vision = models.TextField(default="")
    mission = models.TextField(default="")
    values = models.TextField(default="")
    image = models.ImageField()
    def __str__(self):
        return self.title



class ChooseUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(default="")
    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default_image.jpg')
    icons = models.ImageField(default='icons.jpg')
    subTitle = models.CharField(max_length=300, default="")
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
    footer_text = models.TextField(default="")

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
    facebook = models.URLField(default="")
    x = models.URLField(default="")
    youtube = models.URLField(default="")
    instagram = models.URLField(default="")
    linkedin = models.URLField(default="")
    def __str__(self):
        return self.facebook

class HomeRequest(models.Model):
    info = models.TextField()
    def __str__(self):
        return self.info


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Statistics(models.Model):
    clients = models.IntegerField(default=0)
    projects = models.IntegerField(default=0)
    awards = models.IntegerField(default=0)

    def __str__(self):
        return str(self.projects)
