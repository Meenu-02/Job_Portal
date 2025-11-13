from django.shortcuts import render

from jobapp.models import JobPost


def joblist(request):
    data=JobPost.objects.all()
    return render(request, 'recruiter/joblist.html', {'joblist': data})