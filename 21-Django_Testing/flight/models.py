from django.db import models
from django.contrib.auth.models import User


class Flight(models.Model):
    flight_number = models.CharField(max_length=6)
    airlines = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    date_of_departure = models.DateField()
    etd = models.TimeField()

    def __str__(self):
        return self.flight_number + ' - from ' + self.departure_city + ' to ' + self.arrival_city


class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.last_name} - {self.first_name}"


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE,related_name='reservations_of_flight')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    passenger = models.ManyToManyField(Passenger, related_name='reservations_of_passenger')

    def __str__(self):
        return self.flight.flight_number + ' - ' + self.user.first_name
