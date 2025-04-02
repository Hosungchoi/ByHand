from django.shortcuts import render
from .models import SurveyResponse

def home(request):
    return render(request, 'Palette/home.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse

def submit_survey(request):
    if request.method == "POST":
        feedback = request.POST.get("feedback")
        additional_feedback = request.POST.get("additional_feedback")  # Capture new input
        SurveyResponse.objects.create(feedback=feedback, additional_feedback=additional_feedback)
        return redirect("home")  # Redirect to home or success page
    return render(request, "Palette/survey.html")

def survey_results(request):
    responses = SurveyResponse.objects.all().order_by('-submitted_at')
    return render(request, "Palette/results.html", {"responses": responses})
