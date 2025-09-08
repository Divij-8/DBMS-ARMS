from rest_framework import viewsets
from .models import Scheme, Application
from .serializers import SchemeSerializer, ApplicationSerializer

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all().order_by("-id")
    serializer_class = SchemeSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.select_related("scheme", "farmer").all().order_by("-id")
    serializer_class = ApplicationSerializer
