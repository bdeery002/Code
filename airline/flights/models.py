from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

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