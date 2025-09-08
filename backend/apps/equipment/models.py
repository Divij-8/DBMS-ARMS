from django.db import models
from apps.farmers.models import Farmer

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class RentalRecord(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name="rentals")
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="rentals")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.equipment.name} -> {self.farmer.name}"
