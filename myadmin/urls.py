from django.urls import path
 
from myadmin import views


urlpatterns = [
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("category/", views.category, name="category"),
    path("logout/", views.logout, name="logout"),
    path("add-new/", views.add_new, name="add-new"),
    path("delete_category/<id>/", views.delete_category, name="delete_category"),
    path("update/<id>/", views.update, name="update"),
    path("product/", views.product, name="product"),
    path("add_product/", views.add_product, name="add_product"),
    path("delete_product/<id>/", views.delete_product, name="delete_product"),
    path("update_product/<id>/", views.update_product, name="update_product"),

]