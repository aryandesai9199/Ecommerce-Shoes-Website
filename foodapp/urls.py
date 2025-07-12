from django.urls import path

from foodapp import views


urlpatterns = [
    path('food/',views.food, name="food"),  # Include URLs from foodapp
]