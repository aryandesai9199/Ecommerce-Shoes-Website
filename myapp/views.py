from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is a Django Server")

def new1(request):
    return render(request, "new.html")

# def demo(request):

#     peoples = [
#         {'name':'Aryan', 'age':22},
#         {'name':'jay', 'age':21},
#         {'name':'Kavy', 'age':15},
#         {'name':'Ujef', 'age':23},
#         {'name':'Devansh','age':22}
#     ]

#     for people in peoples:
#         print(people)

#     return render(request, "demo.html", context={'peoples':peoples})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def demo1(request):

    products = [
        {'name':"iphone 16",'price': 68000},
        {'name':"Dell latitude 5400",'price': 48000},
        {'name':"power bank",'price': 2000},
        {'name':"boat airbirds",'price': 2800},
        {'name':"T.V.",'price': 39000},
        {'name':"Frige",'price': 18000},
        {'name':"Cover of iphone 16",'price': 800},
        {'name':"Charging",'price': 3500},
        {'name':"Mouse",'price': 300},
        {'name':"Keybord",'price': 1200},
        {'name':"Samsung S25 FE",'price': 58000},
    ]

    for product in products:
        print(product)

    return render(request,"demo1.html",context={"products":products})


def home1(request):
    return render(request, "home1.html")

def about1(request):
    return render(request, "about1.html")

def contact1(request):
    return render(request, "contact1.html")