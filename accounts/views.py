from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def sign_up(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Регистрация'
        return render(request, 'accounts/sign_up.html', context=data)
    elif request.method == 'POST':
        # Извлечение данных из формы:
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # Каскад проверок данных (валидация):
        if pass1_x != pass2_x:
            data['color_x'] = 'red'
            data['report_x'] = 'Пароли на совпадают!'
        elif pass1_x == '':
            # Остальные проверки ...
            pass
        else:
            # Техническая проверка:
            data['login'] = login_x
            data['pass1'] = pass1_x
            data['pass2'] = pass2_x
            data['email'] = email_x

            # Добавление пользователя в БД:
            user = User.objects.create_user(login_x, email_x, pass1_x)
            user.save()

            # Формирование отчета:
            data['title'] = 'Отчет о регистрации'
            if user is None:
                data['color_x'] = 'red'
                data['report_x'] = 'В регистрации отказано!'
            else:
                data['color_x'] = 'green'
                data['report_x'] = 'Регистрация успешно завершена!'

        return render(request, 'accounts/reports.html', context=data)


def sign_in(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Авторизация'
        return render(request, 'accounts/sign_in.html', context=data)
    elif request.method == 'POST':
        # Получение данных:
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        # Проверка подлинности:
        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            data['color_x'] = 'red'
            data['report_x'] = 'Пользоавтель не найден!'
            data['title'] = 'Отчет об авторизации'
            return render(request, 'accounts/reports.html', context=data)
        else:
            login(request, user)
            return redirect('/home')


def sign_out(request):
    logout(request)
    return redirect('/home')


def profile(request):
    data = dict()
    data['title'] = 'Профиль'
    return render(request, 'accounts/profile.html', context=data)


def ajax_reg(request):
    response = dict()
    login_y = request.GET.get('login')
    try:
        User.objects.get(username=login_y)
        response['message'] = 'занят'
    except User.DoesNotExist:
        response['message'] = 'свободен'
    return JsonResponse(response)
