from django.shortcuts import render

# Create your views here.


def sign_up(request):
    data = {'title': 'Регистрация'}
    return render(request, 'accounts/sign_up.html', context=data)


def sign_in(request):
    data = {'title': 'Авторизация'}
    return render(request, 'accounts/sign_in.html', context=data)


def sign_out(request):
    data = {'title': 'Выход из системы'}
    return render(request, 'accounts/sign_in.html', context=data)








