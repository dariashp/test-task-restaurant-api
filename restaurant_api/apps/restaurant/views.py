import random

from rest_framework.decorators import api_view
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Restaurant
from .serializers import (
    RestaurantSerializer,
    RetrieveRestaurantSerializer,
)


class ListRestaurants(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RetrieveRestaurantSerializer


class RestaurantAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    lookup_url_kwarg = "name"
    lookup_field = "name"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RetrieveRestaurantSerializer
        return RestaurantSerializer


class CreateRestaurantAPIView(CreateAPIView):
    serializer_class = RestaurantSerializer


@api_view(["GET"])
def random_restaurant(request):
    restaurants = Restaurant.objects.all()
    random_restaurant = random.choice(restaurants)
    serializer = RetrieveRestaurantSerializer(random_restaurant)
    return Response(data=serializer.data, status=HTTP_200_OK)
