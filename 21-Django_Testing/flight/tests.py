# from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase
from django.contrib.auth.models import AnonymousUser, User
from .views import FlightView
from rest_framework.test import force_authenticate
from .models import Flight
from django.urls import reverse
from rest_framework.authtoken.models import Token


# Create your tests here.
class FlightTestCase(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='tarik',
            email='tarik@gmail.com',
            password='secret123'
        )
        self.token = Token.objects.get(user=self.user)
        self.flight = Flight.objects.create(
            id=1,
            flight_number="AA100",
            airlines="AHY",
            departure_city="Antalya",
            arrival_city="Amsterdam",
            date_of_departure="2022-12-01",
            etd="15:00:00")


    def test_flight_list_as_guest_user(self):
        request = self.factory.get(reverse('flight-list'))
        request.user = AnonymousUser()
        response = FlightView.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 200)
    
    
    def test_flight_create_as_guest_user(self):
        request = self.factory.post(reverse('flight-list'))
        request.user = AnonymousUser()
        response = FlightView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 401)
    
    
    def test_flight_create_as_login_user(self):
        request = self.factory.post(reverse('flight-list'), HTTP_AUTHORIZATION='Token ' + self.token.key)
        # force_authenticate(request, user=self.user)
        response = FlightView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 403)
    
    
    def test_flight_create_as_admin_user(self):
        data = {
            "flight_number": "TK100",
            "airlines": "THY",
            "departure_city": "Antalya",
            "arrival_city": "Amsterdam",
            "date_of_departure": "2022-12-03",
            "etd": "15:27:22"
        }
        request = self.factory.post(reverse('flight-list'), data, format='json')
        force_authenticate(request, user=self.user)
        self.user.is_staff = True
        self.user.save()
        response = FlightView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)


    def test_flight_update_as_admin_user(self):
        data = {
            "flight_number": "TK100",
            "airlines": "THY",
            "departure_city": "Antalya",
            "arrival_city": "Amsterdam",
            "date_of_departure": "2022-12-03",
            "etd": "15:27:22"
        }
        url = reverse('flight-detail', kwargs={'pk': 1})
        request = self.factory.put(url, data, format='json')
        force_authenticate(request, user=self.user)
        self.user.is_staff = True
        self.user.save()
        response = FlightView.as_view({'put': 'update'})(request, pk='1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Flight.objects.get(id=1).flight_number, 'TK100')
        self.assertEqual(Flight.objects.count(), 1)
