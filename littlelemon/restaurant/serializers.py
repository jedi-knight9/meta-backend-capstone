from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import MenuItem, Booking

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'