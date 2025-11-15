from django.shortcuts import render, get_object_or_404, redirect

from jobapp.models import JobPost, JobApplication, Recruiter, Job_Seeker, Profile, ShortlistedCandidate


def joblist(request):
    data=JobPost.objects.all()
    return render(request, 'recruiter/joblist.html', {'joblist': data})


def view_applicants(request):
    # Get recruiter object from logged-in user
    recruiter = Recruiter.objects.get(user=request.user)

    # Get all jobs posted by this recruiter
    posted_jobs = JobPost.objects.filter(user=recruiter)

    # Get all applications for these jobs
    applications = JobApplication.objects.filter(job__in=posted_jobs)\
                                         .select_related('job', 'seeker')

    return render(request, "recruiter/applied_seeker.html", {
        "applications": applications,
    })

def applicant_profile_view(request,id):
    seeker = Job_Seeker.objects.get(id=id)
    profile = Profile.objects.get(user=seeker)

    return render(request, 'recruiter/applicant_profile.html', {
        'seeker': seeker,
        'profile': profile
    })

def reject_profile(request,id):
    data=JobApplication.objects.get(id=id)
    data.delete()
    return redirect('view_app')


def shortlist_applicant(request,id):
    application = JobApplication.objects.get(id=id)

    # Create a shortlisted entry
    shortlisted = ShortlistedCandidate(
        job=application.job,
        seeker=application.seeker
    )
    shortlisted.save()


    return redirect('view_app')


def shortlist_view(request):
    recruiter = request.user


    recruiter_obj = Recruiter.objects.get(user=recruiter)


    posted_jobs = JobPost.objects.filter(user=recruiter_obj)


    data = ShortlistedCandidate.objects.filter(job__in=posted_jobs)

    return render(request, 'recruiter/shortlist.html', {'shortlist': data})


