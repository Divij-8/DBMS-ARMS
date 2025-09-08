from rest_framework import viewsets
from .models import Crop
from .serializers import CropSerializer

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.select_related("farmer").all().order_by("-id")
    serializer_class = CropSerializer
