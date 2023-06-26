from atexit import register
from rest_framework.routers import DefaultRouter
from .views import FlightView, ReservationView


router = DefaultRouter()
router.register('flights', FlightView)
router.register('reservations', ReservationView)

urlpatterns = router.urls
