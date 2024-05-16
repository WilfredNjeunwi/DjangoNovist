from django.shortcuts import render, HttpResponse
from .models import JobPosting

# Create your views here.
def index(response):
    active_postings= JobPosting.objects.filter(is_active=True)
    context = {
        "job_postings": active_postings,
    }
    return render(response, 'job_board/index.html', context)
