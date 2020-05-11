from django.shortcuts import render, redirect
from hashlib import md5
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def sign_up(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Регистрация'
        return render(request, 'accounts/sign_up.html', context=data)
    elif request.method == 'POST':
        # Извлечение данных из формы
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # Каскад проверок данных (валидация)
        if pass1_x != pass2_x:
            data['color_x'] = 'red'
            data['report_x'] = 'Пароли не совпадают'
        elif pass1_x == '':
            # Остальные проверки...
            pass
        else:
            # Техническая проверка:
            data['login'] = login_x
            data['pass1'] = pass1_x
            data['pass2'] = pass2_x
            data['email'] = email_x

            #  Добавление пользователя в БД:
            user = User.objects.create_user(login_x, email_x, pass1_x)
            user.save()

            # Формирование отчета
            data['title'] = 'Отчет о регистрации'
            if user is None:
                data['color_x'] = 'red'
                data['report_x'] = 'В регистрации отказано!'
            else:
                data['color_x'] = 'green'
                data['report_x'] = 'Регистрация успешно завершена'

        return render(request, 'accounts/report.html', context=data)


def sign_in(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Авторизация'
        return render(request, 'accounts/sign_in.html', context=data)
    elif request.method == 'POST':
        # Проверка данных:
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        # Проверка подленности:
        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            data['color_x'] = 'red'
            data['report'] = 'Пользователь не найден!'
            data['title'] = 'Отчет об авторизации'
            return render(request, 'accounts/sign_in_res.html', context=data)
        else:
            login(request, user)
            return redirect('/home')


def sign_out(request):
    data = {'title': 'Выход из системы'}
    return render(request, 'accounts/sign_in.html', context=data)
