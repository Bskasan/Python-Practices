from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import FlightSerializer, ReservationSerializer
from .models import Flight, Reservation
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated


class FlightView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the reservations
        for the currently authenticated user.
        """
        
        user = self.request.user
        return Reservation.objects.filter(user=user)
