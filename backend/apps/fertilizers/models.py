from django.db import models
from apps.crops.models import Crop

class FertilizerLog(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name="fertilizer_logs")
    type = models.CharField(max_length=128)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    applied_on = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.type} - {self.crop.id}"
