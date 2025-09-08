from rest_framework import viewsets
from .models import Farmer
from .serializers import FarmerSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all().order_by("-id")
    serializer_class = FarmerSerializer
