from rest_framework import viewsets
from .models import Equipment, RentalRecord
from .serializers import EquipmentSerializer, RentalRecordSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all().order_by("-id")
    serializer_class = EquipmentSerializer

class RentalRecordViewSet(viewsets.ModelViewSet):
    queryset = RentalRecord.objects.select_related("equipment", "farmer").all().order_by("-id")
    serializer_class = RentalRecordSerializer
