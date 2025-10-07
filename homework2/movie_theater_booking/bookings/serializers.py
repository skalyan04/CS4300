# bookings/serializers.py
from rest_framework import serializers
from .models import Movie, Seat, Booking

# Serializer for Movie model
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# Serializer for Seat model
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

# Serializer for Booking model
class BookingSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    seat = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all())
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'
