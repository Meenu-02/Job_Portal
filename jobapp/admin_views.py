# admin_views.py or in your existing admin file

from django.shortcuts import render

from jobapp.filters import JobFilter, ShortlistFilter
from jobapp.models import JobPost, ShortlistedCandidate


def admin_job_list(request):
    jobs = JobPost.objects.all()
    jobFilter = JobFilter(request.GET, queryset=jobs)
    s = jobFilter.qs
    context = {
        'jobs': s,
        'jobFilter': jobFilter
    }

    return render(request, 'admin/job_list.html', context)

def admin_job_details(request, id):
    job = JobPost.objects.get(id=id)
    return render(request, 'admin/job_details.html', {'details': job})

def admin_shortlisted_candidates(request):
    data = ShortlistedCandidate.objects.all()
    shortlistFilter = ShortlistFilter(request.GET, queryset=data)
    s = shortlistFilter.qs
    context = {'shortlisted': s,
               'shortlistFilter': shortlistFilter}

    return render(request, "admin/shortlisted_list.html", context)
