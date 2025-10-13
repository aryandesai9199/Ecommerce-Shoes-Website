from django.shortcuts import render, redirect
from .models import *
from myadmin.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from myadmin.models import *
from django.http import JsonResponse

# Create your views here.   


def home(request):
    dynemic = Product.objects.filter(prdFeature = 1)[:4]
    dynemicLatest = Product.objects.filter(prdLatest = 1)[:4]
    return render(request, 'home.html', {'dynemic': dynemic,'dynemicLatest':dynemicLatest})


def cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    for product in products:
        cart_items.append({
            'product': product,
            'quantity': cart[str(product.id)],
        })
    return render(request, 'cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return JsonResponse({'success': True, 'cart': cart})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return JsonResponse({'success': True, 'cart': cart})

def update_cart(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[str(product_id)] = quantity
    else:
        cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return JsonResponse({'success': True, 'cart': cart})

def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    for product in products:
        cart_items.append({
            'product': product,
            'quantity': cart[str(product.id)],
        })
    return render(request, 'cart.html', {'cart_items': cart_items})


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
    return render(request, 'view_detail_blog.html',{'dy_detail':dynemic})

def view_details_product(request, id):
    dynemic = Product.objects.filter(id = id)
    return render(request, 'view_detail_product.html',{'dy_detail':dynemic})

def Category_collection(request):
    dynemicMale = Product.objects.filter(prdCatMale = 1)
    dynemicFemale = Product.objects.filter(prdCatFemale = 1)
    return render(request, 'Category_collection.html', {'dynemicMale':dynemicMale , 'dynemicFemale':dynemicFemale})
