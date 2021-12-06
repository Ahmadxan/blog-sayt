from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm, ContactForm
from post.models import Blog


def login_page(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home-page')

    return render(request, 'registration/login.html')


def logout_page(request):
    logout(request)
    return redirect('home-page')


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


def home_page(request):
    form = ContactForm(request.POST)
    if request.POST and form.is_valid():
        form.author = request.user
        form.save()
    blog_list = Blog.objects.all()

    return render(request, 'index.html', {'form': form, "blog_list": blog_list})


def about_page(request):
    return render(request, 'about.html')


def blog_page(request):
    return render(request, 'blog.html')


def add_blog(request):
    return render(request, 'add-blog.html')


def contact_page(request):
    form = ContactForm(request.POST)
    if request.POST and form.is_valid():
        form.author = request.user
        form.save()

    return render(request, 'contact.html', {'form': form})
