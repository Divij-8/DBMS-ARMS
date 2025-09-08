from django.db import models
from apps.farmers.models import Farmer

class Crop(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="crops")
    name = models.CharField(max_length=255)
    season = models.CharField(max_length=64, blank=True)
    sown_date = models.DateField(null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.farmer.name}"
