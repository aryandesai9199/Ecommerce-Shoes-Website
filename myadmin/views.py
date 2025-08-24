from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse

from myadmin.models import AdminUserMaster, CategoryMaster

# Create your views here.


def login(request):
    if request.session.get("name"):
        return redirect("/myadmin/dashboard")
    if request.method == 'POST':
        mstName = request.POST.get('mstName')
        mstPassword = request.POST.get('mstPassword')
        mstEmail = request.POST.get('mstEmail')
        print(mstName)
        print(mstPassword)
        user = AdminUserMaster.objects.filter(mstName=mstName,mstPassword=mstPassword).first()
        if user:
            request.session["name"]=user.mstName
            request.session["email"]=user.mstEmail
            response = HttpResponse("set cookies")
            response = redirect("/myadmin/dashboard/")
            response.set_cookie("name",user.mstName,max_age=3600)
            return response
            
        else:
            return render(request, 'login_page.html', {'error': 'Invalid credentials'})
    return render(request, 'login_page.html')

def dashboard(request):
    if request.session.get("name"):
        return render(request, 'dashboard.html')
    else:
        return redirect("/myadmin/login/")
    # name = request.COOKIES.get("name")
    # return render(request, "dashboard.html", {"username":name})
    
def mstPage(request):
    category_datas = CategoryMaster.objects.all()
    return render(request, "master_page.html",context={"category_dats":category_datas})


def category(request):
    category_datas = CategoryMaster.objects.all()
    if request.session.get("name"):
        return render(request, 'Category_page.html',context={'category_datas':category_datas})
    else:
        return redirect("/myadmin/login/")

def logout(request):
    request.session.flush()
    return redirect('/myadmin/login/')


def add_new(request):
    if request.method == 'POST':
        catName = request.POST.get('catName')
        catImage = request.FILES.get('catImage')
        catStatus = request.POST.get('catStatus') == 'True'
        catSlug = catName.lower().replace(" "," -")

        CategoryMaster.objects.create(
            catName = catName,
            catImage = catImage,
            catStatus = catStatus,
            catSlug = catSlug,
        )

        return redirect("/myadmin/category/")


    return render(request, "Add_new.html")

def delete_category(request, id):
    queryset = CategoryMaster.objects.get(id = id)
    queryset.delete()
    return redirect("/myadmin/category/")

from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def update(request, id):
    if not request.session.get("name"):
        return redirect("/myadmin/login/")
    category = get_object_or_404(CategoryMaster, id=id)

    if request.method == "POST":
        category.catName = request.POST.get('catName')
        category.catSlug = category.catName.lower().replace(" ","-")
        category.catStatus = request.POST.get('catStatus') == 'on'

        if 'catImage' in request.FILES:
            category.catImage = request.FILES['catImage']

        category.save()
        return redirect('/myadmin/category/')

    return render(request, 'update_category.html', context={"category": category})


def product(request):
    if not request.session.get("name"):
        return redirect("/myadmin/login/")
    products = Product.objects.all()
    return render(request, "product.html",context={"products": products})

def add_product(request):
    if not request.session.get("name"):
        return redirect("/myadmin/login/")
    if request.method == "POST":
        prdName = request.POST.get('prdName')
        prdDescription = request.POST.get('prdDescription')
        prdPrice = request.POST.get('prdPrice')
        prdIsoffer = request.POST.get('prdIsoffer')
        prdOfferPrice = request.POST.get('prdOfferPrice')
        prdImage = request.FILES.get('prdImage')
        prdLatest = request.POST.get('prdLatest') is not None
        prdFeature = request.POST.get('prdFeature') is not None
        prdBlog = request.POST.get('prdBlog') is not None
        prdMailDes = request.POST.get('prdMailDes')


        Product.objects.create(
            prdName = prdName,
            prdDescription = prdDescription,
            prdPrice = prdPrice,
            prdIsoffer = prdIsoffer,
            prdOfferPrice = prdOfferPrice,
            prdImage = prdImage,
            prdLatest = prdLatest,
            prdFeature = prdFeature,
            prdBlog = prdBlog,
            prdMailDes = prdMailDes
        )
        return redirect("/myadmin/product/")
    return render(request, "add_product.html")

def delete_product(request, id):
    if not request.session.get("name"):
        return redirect("/myadmin/login/")
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("/myadmin/product/")

def update_product(request, id):
    if not request.session.get("name"):
        return redirect("/myadmin/login/")
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.prdName = request.POST.get("prdName")
        product.prdDescription = request.POST.get("prdDescription")
        product.prdPrice = request.POST.get("prdPrice")
        product.prdIsoffer = 'prdIsoffer' in request.POST
        product.prdOfferPrice = request.POST.get("prdOfferPrice")
        product.prdLatest = 'prdLatest' in request.POST
        product.prdFeature = 'prdFeature' in request.POST
        product.prdBlog = 'prdBlog' in request.POST
        product.prdMailDes = request.POST.get("prdMailDes")
        if 'prdImage' in request.FILES:
            product.prdImage = request.FILES["prdImage"]
        product.save()
        return redirect("/myadmin/product/")
    return render(request, "update_product.html",context={"product":product})

