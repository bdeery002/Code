from django.contrib import admin
from .models import User, Listing, Bid, Comment

# This helps you see more information in the list view
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "starting_bid", "is_active", "category")

class BidAdmin(admin.ModelAdmin):
    list_display = ("user", "listing", "amount")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "listing", "text")

# Register your models here.
admin.site.register(User)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)