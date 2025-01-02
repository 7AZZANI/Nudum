from django.shortcuts import render

def mainpage(request):
    return render(request, 'single-index2.html')

def developtment_services(request):
    return render(request, 'service2.html')

def soft_development(request):
    return render(request, 'service-details2.html')
