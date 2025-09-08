from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.farmers.views import FarmerViewSet
from apps.crops.views import CropViewSet
from apps.fertilizers.views import FertilizerLogViewSet
from apps.equipment.views import EquipmentViewSet, RentalRecordViewSet
from apps.schemes.views import SchemeViewSet, ApplicationViewSet
from apps.reports.views import SummaryView

router = DefaultRouter()
router.register(r'farmers', FarmerViewSet, basename='farmer')
router.register(r'crops', CropViewSet, basename='crop')
router.register(r'fertilizer-logs', FertilizerLogViewSet, basename='fertilizerlog')
router.register(r'equipment', EquipmentViewSet, basename='equipment')
router.register(r'rentals', RentalRecordViewSet, basename='rentalrecord')
router.register(r'schemes', SchemeViewSet, basename='scheme')
router.register(r'scheme-applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/reports/summary/', SummaryView.as_view(), name='summary'),
    path('api/auth/', include('rest_framework.urls')),
]
