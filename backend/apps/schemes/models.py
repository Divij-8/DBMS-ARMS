from django.db import models
from apps.farmers.models import Farmer

class Scheme(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title

class Application(models.Model):
    STATUS_CHOICES = [("pending","Pending"),("approved","Approved"),("rejected","Rejected")]
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE, related_name="applications")
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="scheme_applications")
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="pending")
    applied_on = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.farmer.name} -> {self.scheme.title} ({self.status})"
