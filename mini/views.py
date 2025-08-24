from django.shortcuts import render, redirect
from .models import *
from myadmin.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from myadmin.models import *

# Create your views here.   


def home(request):
    dynemic = Product.objects.filter(prdFeature = 1)[:4]
    dynemicLatest = Product.objects.filter(prdLatest = 1)[:4]
<<<<<<< HEAD
    return render(request, 'home.html', {'dynemic': dynemic,'dynemicLatest':dynemicLatest})
=======
    return render(request, 'index.html', {'dynemic': dynemic,'dynemicLatest':dynemicLatest})
>>>>>>> de1bc3b6e4a8f1ef05c08c251033e3cd2bdd649e



def login1(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            pwd = check_password(password, user.password)
            if pwd:
                return redirect("/home/")
            else:
                return render(request, 'Login1.html', {'error': 'Invalid password.'})
    return render(request, 'Login1.html')


def register1(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if name and email and username and password:
            user = User.objects.create_user(
                first_name = name,
                email=email,
                username=username,
                password=password
            )
            user.save()
            return render(request, 'login1.html', {'message': 'User created successfully!'})
        else:
            return render(request, 'register1.html', {'error': 'All fields are required.'})

    return render(request, 'register1.html')

def about(request):
    return render(request, 'About_Mini.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        con_us.objects.create(
            name=name,
            email=email,
            message=message
        )
    return render(request, 'Contact_Mini.html')

def shop(request):
    dynemic = Product.objects.filter(prdFeature = 1)
    dynemicLatest = Product.objects.filter(prdLatest = 1)
    return render(request, 'Shop_mini.html', {'dynemic': dynemic,'dynemicLatest':dynemicLatest})

def page(request):
    dynemic = Product.objects.filter(prdBlog = 1)
    return render(request, "page_blog_mini.html",{'DynemicBlog':dynemic})

def views_details_blog(request, id):
    dynemic = Product.objects.filter(prdBlog = 1 ,id = id)
<<<<<<< HEAD

    return render(request, 'view_detail_blog.html',{'dy_detail':dynemic})
=======
    return render(request, 'view_detail_blog.html',{'dy_detail':dynemic})
>>>>>>> de1bc3b6e4a8f1ef05c08c251033e3cd2bdd649e
