from django.contrib import admin

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
    Appointment,
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


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=["phone", "email", "location", ]

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=["author", "title", "subTitle", "content", "timestamp",  ]




@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=["name", "email", "contact", "date", "time", "message" ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=["title", "description", ]

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
