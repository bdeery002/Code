from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
# 1. NEW MODEL: The Business Process (e.g., Procure to Pay)
class BusinessProcess(models.Model):
    name = models.CharField(max_length=100) # e.g., "Procure to Pay"
    slug = models.SlugField(unique=True)     # e.g., "p2p"
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Business Process"
        verbose_name_plural = "Business Processes"

    def __str__(self):
        return self.name

# 2. UPDATED MODEL: Link SoxControl to BusinessProcess
class SoxControl(models.Model):
    control_id = models.CharField(max_length=50, unique=True)
    
    # NEW: Link to the BusinessProcess model
    process = models.ForeignKey(
        BusinessProcess, 
        on_delete=models.CASCADE, 
        related_name="controls",
        null=True, # Allow null temporarily so migrations don't break existing data
        blank=True
    )
    
    # We keep sub_process as a text field for granular SVG filtering
    sub_process = models.CharField(max_length=200, blank=True, null=True)
    
    control_description = models.TextField()
    
    RISK_CHOICES = [
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]
    risk = models.CharField(max_length=100, choices=RISK_CHOICES)
    effective_date = models.DateField()

    class Meta:
        verbose_name = "SOX Control"
        verbose_name_plural = "SOX Controls"

    def __str__(self):
        return f"{self.control_id} - {self.sub_process}"


# Airport model
class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['code']
        verbose_name = "Airport"
        verbose_name_plural = "Airports"
    
    def __str__(self):
        return f"{self.code} ({self.city})"

# Flight model
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField(help_text="Duration in minutes")
    
    class Meta:
        ordering = ['origin', 'destination']
        verbose_name = "Flight"
        verbose_name_plural = "Flights"
    
    def __str__(self):
        return f"{self.origin} to {self.destination}"
    
    def clean(self):
        """Validate the model fields"""
        if self.duration <= 0:
            raise ValidationError("Duration must be positive")
        if self.origin == self.destination:
            raise ValidationError("Origin and destination cannot be the same")
    
    def save(self, *args, **kwargs):
        """Override save to call clean()"""
        self.full_clean()
        super().save(*args, **kwargs)

class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    flights = models.ManyToManyField(
        Flight,
        blank=True,
        related_name="passengers",
    )

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Passenger"
        verbose_name_plural = "Passengers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"