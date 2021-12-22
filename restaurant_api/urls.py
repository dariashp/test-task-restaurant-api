from django.contrib import admin
from django.urls import path, include

from .apps.restaurant.urls import urlpatterns as restaurant_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include(restaurant_urls))
]
