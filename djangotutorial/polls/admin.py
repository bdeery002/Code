from django.contrib import admin
from .models import Question, Choice


# This allows you to edit choices right inside the Question page
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # This is the magic line that adds columns to your list view
    list_display = ["question_text", "pub_date", "was_published_recently"]
    
    # This adds a sidebar filter
    list_filter = ["pub_date"]
    
    # This adds a search bar at the top
    search_fields = ["question_text"]
    
    inlines = [ChoiceInline]

# Register your models here.
admin.site.register(Question, QuestionAdmin)