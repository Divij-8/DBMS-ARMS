from rest_framework import viewsets
from .models import FertilizerLog
from .serializers import FertilizerLogSerializer

class FertilizerLogViewSet(viewsets.ModelViewSet):
    queryset = FertilizerLog.objects.select_related("crop").all().order_by("-id")
    serializer_class = FertilizerLogSerializer
