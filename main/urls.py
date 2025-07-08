from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about-us", views.about, name="about"),
    path("contact-us", views.contact, name="contact"),
    path("services", views.service, name="service"),
    path("blog", views.blog, name="blog"),
    path("blog-details/<id>", views.blog_details, name="details"),
    path("services-details/<id>", views.service_details, name="service-details"),
    path("testimonials", views.testimonails, name="testimonails"),
    path("sendmessage", views.send_message, name="sendmessage"),
    path("bookappointment", views.book_appointment, name="bookappointment"),
    path(".well-known/acme-challenge/<slug>", views.well_known, name="wellknown"),
]
