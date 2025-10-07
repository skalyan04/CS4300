from django.shortcuts import render
from .models import Movie
from django.utils import timezone
# bookings/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Movie API view
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Seat API view
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    # Custom action to book a seat
    @action(detail=True, methods=['post'])
    def book(self, request, pk=None):
        seat = get_object_or_404(Seat, pk=pk)
        if seat.is_booked:
            return Response({'error': 'Seat already booked'}, status=status.HTTP_400_BAD_REQUEST)
        seat.is_booked = True
        seat.save()
        return Response({'success': f'Seat {seat.seat_number} booked'})

# Booking API view
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# --- Views for templates ---

# Show movies
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

# Show seats and handle booking
@login_required
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()
    # Get all available seats
    available_seats = Seat.objects.filter(is_booked=False)
    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        seat = get_object_or_404(Seat, id=seat_id)
        if not seat.is_booked:
            seat.is_booked = True
            seat.save()
            Booking.objects.create(movie=movie, seat=seat, user=request.user, booking_date=timezone.now)
            return redirect('booking_history')
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

# Show booking history
@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})# Create your views here.
