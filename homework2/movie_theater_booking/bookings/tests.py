from django.test import TestCase

# bookings/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Movie, Seat, Booking

class MovieModelTest(TestCase):
    """Test the Movie model"""
    def test_create_movie(self):
        movie = Movie.objects.create(
            title="Test Movie",
            description="A test description",
            release_date="2025-10-01",
            duration=120
        )
        self.assertEqual(movie.title, "Test Movie")
        self.assertEqual(movie.duration, 120)

class SeatModelTest(TestCase):
    """Test the Seat model"""
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="A1")

    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertFalse(self.seat.is_booked)

class BookingModelTest(TestCase):
    """Test the Booking model"""
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test description",
            release_date="2025-10-01",
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="A1")

    def test_create_booking(self):
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user,
            booking_date=timezone.now()
        )
        self.seat.is_booked = True
        self.seat.save()

        self.assertTrue(booking.seat.is_booked)
        self.assertEqual(booking.movie.title, "Test Movie")
        self.assertEqual(booking.user.username, "testuser")

class MovieAPITest(APITestCase):
    """Test Movie API endpoints"""
    def setUp(self):
        self.movie = Movie.objects.create(
            title="API Movie",
            description="API test description",
            release_date="2025-10-01",
            duration=120
        )

    def test_get_movies_list(self):
        url = reverse('movie-list')  # Uses DRF router name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "API Movie")

class BookingAPITest(APITestCase):
    """Test Booking API endpoints"""
    def setUp(self):
        self.user = User.objects.create_user(username='apiuser', password='password')
        self.movie = Movie.objects.create(
            title="Booking Movie",
            description="Booking test description",
            release_date="2025-10-01",
            duration=90
        )
        self.seat = Seat.objects.create(seat_number="B1")

    def test_create_booking(self):
        url = reverse('booking-list')  # DRF router name for bookings
        self.client.force_authenticate(user=self.user)
        data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "booking_date": timezone.now().isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Booking.objects.filter(user=self.user, movie=self.movie).exists())
