from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from .models import JobPosting


# Create your views here.
def index(response):
    active_postings= JobPosting.objects.filter(is_active=True)
    context = {
        "job_postings": active_postings,
    }
    return HttpResponse(context)

def job_detail(response, pk):
    # job_posting = JobPosting.objects.get(id=pk)
    job_posting = get_object_or_404(JobPosting, pk=pk, is_active=True)
    context = {
        "posting": job_posting,
    }
    return render(response, 'job_board/detail.html', context)
