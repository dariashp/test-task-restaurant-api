from rest_framework import serializers
from rest_framework.fields import CharField

from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RetrieveRestaurantSerializer(RestaurantSerializer):
    type = CharField(source="get_type")
