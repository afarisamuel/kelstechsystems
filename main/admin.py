from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.
from main.models import (
    HomeCarousel,
    About,
    ContactUs,
    Service,
    Team,
    Testimonials,
    BlogPost,
    ChooseUs,
    Message,
    SocialLink,
    Appointment, HomeRequest,
)


admin.site.site_header  = "Kelstech Systems Administration"
admin.site.site_title   = "Kelstech Systems Administration"





@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display=["clientName", "clientProfession", "message" ]




@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display=["title", "link", ]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=["name", "role", ]

@admin.register(HomeRequest)
class HomeRequestAdmin(admin.ModelAdmin):
    list_display=["info", ]

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=["phone", "email", "location", ]

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    list_display=["author", "title", "subTitle", "timestamp",  ]




@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=["name", "email", "contact", "date", "time", "message" ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    list_display=["title", "subTitle", ]


@admin.register(ChooseUs)
class ChooseUsAdmin(admin.ModelAdmin):
    list_display=["title", "description", ]



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=["title", "description", ]

@admin.register(HomeCarousel)
class HomeCarouselAdmin(admin.ModelAdmin):
    list_display=["title", "description", ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=["name", "email", "subject", "message"]
