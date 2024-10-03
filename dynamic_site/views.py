from django.shortcuts import render 
from .models import Carousel, Intro, Story, Mission, Vision, Service, Stat, CompanyProfile, Copyright, Navbar

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def home(request):
    carousels = Carousel.objects.all()
    intro = Intro.objects.first()
    story = Story.objects.first()
    mission = Mission.objects.first()
    vision = Vision.objects.first()
    services = Service.objects.all()
    stats = Stat.objects.all()
    company_profile = CompanyProfile.objects.first()
    copyright_text = Copyright.objects.first()
    navbar = Navbar.objects.all()
    
    

    context = {
        'carousels': carousels,
        'intro': intro,
        'story': story,
        'mission': mission,
        'vision': vision,
        'services': services,
        'stats': stats,
        'company_profile': company_profile,
        'copyright': copyright_text,
        'navbar': navbar
    }

    return render(request, 'home.html', context)
