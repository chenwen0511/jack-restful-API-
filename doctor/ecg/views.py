from rest_framework import viewsets
from rest_framework.response import Response
from .models import Doctor

from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
