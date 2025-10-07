# bookings/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, book_seat, booking_history

router = DefaultRouter()
router.register(r'api/movies', MovieViewSet)
router.register(r'api/seats', SeatViewSet)
router.register(r'api/bookings', BookingViewSet)

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/book/', book_seat, name='book_seat'),

    # Template views
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/book/', book_seat, name='book_seat'),
    path('booking-history/', booking_history, name='booking_history'),
]
