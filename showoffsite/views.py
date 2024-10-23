from django.shortcuts import render

def mainpage(request):
    return render(request, 'single-index2.html')