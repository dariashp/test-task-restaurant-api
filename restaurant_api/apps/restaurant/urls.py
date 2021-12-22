from django.urls import path

from .views import ListRestaurants, RestaurantAPIView, CreateRestaurantAPIView, random_restaurant

urlpatterns = [
    path("list/", ListRestaurants.as_view()),
    path("random/", random_restaurant),
    path("<str:name>/", RestaurantAPIView.as_view()),
    path("", CreateRestaurantAPIView.as_view())
]