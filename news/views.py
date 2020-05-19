from django.shortcuts import render, redirect
from .forms import PostForm, PostForm2
from .models import Post
from django.contrib.auth import logout
from django.core.paginator import Paginator



# Create your views here.


def index(request):
    data = dict()
    data['title'] = 'Лента новостей'
    all_posts = Post.objects.all()
    data['posts'] = all_posts

    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj

    return render(request, 'news/index.html', context=data)





def create(request):
    data = dict()
    data['title'] = 'Добавление новости'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку!
        # =========================================
        if request.user.username == 'admin':
            data['form'] = PostForm()
            return render(request, 'news/create.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
        # =========================================
    elif request.method == 'POST':
        filled_form = PostForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/news')


def details(request, post_id):
    data = dict()
    data['title'] = 'Просмотр новости'
    data['post'] = Post.objects.get(id=post_id)
    return render(request, 'news/details.html', context=data)


def edit(request, post_id):
    data = dict()
    data['title'] = 'Редактирование новости'
    post = Post.objects.get(id=post_id)
    # del ...
    if request.method == 'GET':
        data['form'] = PostForm2(instance=post)
        data['post'] = post
        return render(request, 'news/edit.html', context=data)
    elif request.method == 'POST':
        form2 = PostForm2(request.POST)
        if form2.is_valid():
            post.title = form2.cleaned_data['title']
            post.about = form2.cleaned_data['about']
            post.content = form2.cleaned_data['content']
            post.author = form2.cleaned_data['author']
            post.source = form2.cleaned_data['source']
            post.save()
            # update ?
        return redirect('/news')



def delete(request, post_id):
    data = dict()
    data['title'] = 'Удаление новости'
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        data['post'] = post
        return render(request, 'news/delete.html', context=data)
    elif request.method == 'POST':
        post.delete()
        return redirect('/news')
