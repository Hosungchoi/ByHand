from django.db import models

class SurveyResponse(models.Model):
    feedback = models.TextField()
    additional_feedback = models.TextField(blank=True, null=True)  # New question
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Survey Response {self.id} - {self.submitted_at}"
