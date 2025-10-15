"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from myapp import views
# from foodapp import views
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mini import views
# from my_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Home page url
    path('foodapp/',include('foodapp.urls')),  # Include URLs from foodapp
    
    # path("home/", views.home, name="home"),
    # path("demo1/", views.demo1, name="demo1"),
    # path("new1/", views.new1, name="new1"),
    # path("about/", views.about, name="about"),
    # path("contact/", views.contact, name="contact"),
    # path("home1/", views.home1, name="home1"),
    # path("about1/", views.about1, name="about1"),
    # path("contact1/", views.contact1, name="contact1"),


    # path("food/",views.food,name="food"),
    # path("aryan/",views.aryan, name="aryan"),
    # path('food/delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    # path('food/update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),


    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('home/view-detail/<id>/',views.view_details_product, name='view-product'),
    path('login1/',views.login1, name='login1'),
    path('register1/',views.register1, name='register1'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('shop/',views.shop, name='shop'),
    path("page/", views.page, name="page"),
    path("page/view-detail/<id>/",views.views_details_blog, name='view-more'),
    path('shop/category/', views.Category_collection, name='Category_collection'),
    path("shop/category/view-detail/<id>/",views.view_details_product, name='view-product'),

    path('view-cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    
    path('myadmin/',include('myadmin.urls')), 

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)