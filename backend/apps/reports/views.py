from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.farmers.models import Farmer
from apps.crops.models import Crop
from apps.fertilizers.models import FertilizerLog
from apps.equipment.models import Equipment, RentalRecord
from apps.schemes.models import Scheme, Application

class SummaryView(APIView):
    def get(self, request):
        data = {
            "farmers": Farmer.objects.count(),
            "crops": Crop.objects.count(),
            "fertilizer_logs": FertilizerLog.objects.count(),
            "equipment": Equipment.objects.count(),
            "rentals": RentalRecord.objects.count(),
            "schemes": Scheme.objects.count(),
            "applications": Application.objects.count(),
        }
        return Response(data)
