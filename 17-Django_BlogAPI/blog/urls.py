from django.urls import path
# Routers;
from rest_framework.routers import DefaultRouter
from blog.views import CategoryView, PostView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('post', PostView)

urlpatterns = router.urls