from django.shortcuts import render

# Create your views here.


def menu(request):
    return render(request, 'base.html')
