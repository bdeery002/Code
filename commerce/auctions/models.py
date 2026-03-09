
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing', blank=True, related_name="watchlisted_by")

class Listing(models.Model):

    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=64, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="listings")

    def save(self, *args, **kwargs):
        # Logic: If no one has bid yet, the current price is the starting price
        if self.current_price is None:
            self.current_price = self.starting_bid
        super().save(*args, **kwargs)

class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True) # Good to know when it was posted

    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}"
