from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from jobapp.filters import ShortlistFilter
from jobapp.models import JobPost, JobApplication, Recruiter, Job_Seeker, Profile, ShortlistedCandidate


# def joblist(request):
#     data=JobPost.objects.all()
#     return render(request, 'recruiter/joblist.html', {'joblist': data})


@login_required(login_url='login_view')
def joblist(request):
    recruiter = get_object_or_404(Recruiter, user=request.user)
    data = JobPost.objects.filter(user=recruiter)
    return render(request, 'recruiter/joblist.html', {'joblist': data})


@login_required(login_url='login_view')
def view_applicants(request):
    recruiter = Recruiter.objects.get(user=request.user)
    posted_jobs = JobPost.objects.filter(user=recruiter)
    applications = JobApplication.objects.filter(job__in=posted_jobs)\
                                         .select_related('job', 'seeker')

    return render(request, "recruiter/applied_seeker.html", {
        "applications": applications,
    })

@login_required(login_url='login_view')
def applicant_profile_view(request,id):
    seeker = Job_Seeker.objects.get(id=id)
    profile = Profile.objects.get(user=seeker)

    return render(request, 'recruiter/applicant_profile.html', {
        'seeker': seeker,
        'profile': profile
    })

@login_required(login_url='login_view')
def reject_profile(request,id):
    data=JobApplication.objects.get(id=id)
    data.delete()
    return redirect('view_app')

@login_required(login_url='login_view')
def shortlist_applicant(request,id):
    application = JobApplication.objects.get(id=id)
    shortlisted = ShortlistedCandidate(
        job=application.job,
        seeker=application.seeker
    )
    shortlisted.save()


    return redirect('view_app')

@login_required(login_url='login_view')
def shortlist_view(request):
    recruiter = request.user
    recruiter_obj = Recruiter.objects.get(user=recruiter)
    posted_jobs = JobPost.objects.filter(user=recruiter_obj)
    data = ShortlistedCandidate.objects.filter(job__in=posted_jobs)
    shortlistFilter = ShortlistFilter(request.GET, queryset=data)
    s = shortlistFilter.qs
    context=  {'shortlist': s,
        'shortlistFilter': shortlistFilter}

    return render(request, 'recruiter/shortlist.html',context)



