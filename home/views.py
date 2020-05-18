from django.shortcuts import render

# Create your views here.


def index(request):
    data = {'title': 'Главная'}
    return render(request, 'home/index.html', context=data)


def about(request):
    data = {'title': 'Про сайт'}
    return render(request, 'home/about.html', context=data)


def contacts(request):
    data = {'title': 'Контакты'}
    return render(request, 'home/contacts.html', context=data)
