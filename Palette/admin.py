from django.contrib import admin
from .models import SurveyResponse

@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'submitted_at', 'feedback', 'additional_feedback')
    search_fields = ('feedback', 'additional_feedback')
    list_filter = ('submitted_at',)
