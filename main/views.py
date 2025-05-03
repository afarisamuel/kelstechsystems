from django.core.exceptions import RequestDataTooBig
from django.shortcuts import redirect, render, get_object_or_404

from main.models import (
    Appointment,
    HomeCarousel,
    About,
    ContactUs,
    Message,
    Service,
    Team,
    Testimonials,
    BlogPost,
    ChooseUs, HomeRequest,
)


# Create your views here.
def index(request):
    carousels = HomeCarousel.objects.all()
    abouts = About.objects.all()
    home_info = HomeRequest.objects.all()
    contacts = ContactUs.objects.all()
    chooses = ChooseUs.objects.all()
    services = Service.objects.all()
    testimonails = Testimonials.objects.all()
    teams = Team.objects.all()
    blogs = BlogPost.objects.all()
    about = None
    home = None
    contact = None
    if len(abouts) > 0:
        about = abouts[0]
    if len(contacts) > 0:
        contact = contacts[0]
    if len(home_info) > 0:
        home = home_info[0]
    context = {
        "carousels": carousels,
        "about": about,
        "chooses": chooses,
        "services": services,
        "contact": contact,
        "testimonails": testimonails,
        "teams": teams,
        "blogs": blogs,
        "home": home,
    }
    return render(request, "main/index.html", context)


def about(request):
    teams = Team.objects.all()
    abouts = About.objects.all()
    contacts = ContactUs.objects.all()
    services = Service.objects.all()
    about = None
    contact = None
    if len(abouts) > 0:
        about = abouts[0]
    if len(contacts) > 0:
        contact = contacts[0]

    context = {
        "teams": teams,
        "about": about,
        "contact": contact,
        "services": services,
    }
    return render(request, "main/about.html", context)


def contact(request):
    contacts = ContactUs.objects.all()
    services = Service.objects.all()
    contact = None
    if len(contacts) > 0:
        contact = contacts[0]
    context = {
        "contact": contact,
        "services": services,
    }
    return render(request, "main/contact.html", context)


def service(request):
    services = Service.objects.all()
    testimonails = Testimonials.objects.all()
    contacts = ContactUs.objects.all()


    contact = None
    if len(contacts) > 0:
        contact = contacts[0]
    context = {
        "services": services,
        "testimonails": testimonails,
        "contact": contact,
    }
    return render(request, "main/service.html", context)


def blog(request):
    blogs = BlogPost.objects.all().order_by("-timestamp")
    contacts = ContactUs.objects.all()
    services = Service.objects.all()
    contact = None
    if len(contacts) > 0:
        contact = contacts[0]
    context = {
        "blogs": blogs,
        "contact": contact,
        "services": services,
    }
    return render(request, "main/blog.html", context)


def testimonails(request):
    contacts = ContactUs.objects.all()
    services = Service.objects.all()
    contact = None
    if len(contacts) > 0:
        contact = contacts[0]
    context = {"contact": contact, "services": services,}
    return render(request, "main/testimonial.html", context)


def blog_details(request, id):
    blogs = BlogPost.objects.all().order_by("-timestamp")
    services = Service.objects.all()
    blog = get_object_or_404(BlogPost, pk=id)
    contacts = ContactUs.objects.all()

    contact = None
    if len(contacts) > 0:
        contact = contacts[0]
    context = {
        "blog": blog,
        "contact": contact,
        "blogs": blogs,
        "services": services,
    }

    return render(request, "main/detail.html", context)

def service_details(request, id):
    services = Service.objects.all()
    service = get_object_or_404(Service, pk=id)
    contacts = ContactUs.objects.all()

    contact = None
    if len(contacts) > 0:
        contact = contacts[0]
    context = {
        "service": service,
        "contact": contact,
        "services": services,
    }

    return render(request, "main/service_detail.html", context)

def send_message(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        message = Message(
            message=message,
            name=name,
            email=email,
            subject=subject,
        )
        message.save()
    else:
        print("GET")
    return redirect('/contact-us')


def book_appointment(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        message = request.POST["message"]

        time = request.POST["time"]
        date = request.POST["date"]

        appointment = Appointment(
            name=name,
            email=email,
            contact=contact,
            message=message,
            time=time,
            date=date
        )
        appointment.save()

    return redirect("/")
