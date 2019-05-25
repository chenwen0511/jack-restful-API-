from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

router = DefaultRouter()
router.register(r'doctor', views.DoctorViewSet, basename='doctor')
urlpatterns = router.urls
