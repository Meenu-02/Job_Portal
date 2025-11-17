from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from jobapp.filters import JobFilter
from jobapp.forms import ProfileForm
from jobapp.models import JobPost, Profile, Job_Seeker, JobApplication, ShortlistedCandidate

@login_required(login_url='login_view')
def jobs(request):
    data=JobPost.objects.all()
    jobFilter = JobFilter(request.GET, queryset=data)
    s = jobFilter.qs
    context = {
        'jobs': s,
        'jobFilter': jobFilter
    }

    return render(request, 'seeker/jobs.html', context)

@login_required(login_url='login_view')
def job_details(request,id):
    data=JobPost.objects.get(id=id)
    return render(request,'seeker/job_details.html',{'details':data})

@login_required(login_url='login_view')
def profile(request):
    seeker = get_object_or_404(Job_Seeker, user=request.user)

    profile_instance, created = Profile.objects.get_or_create(user=seeker)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile_instance)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
             form = ProfileForm(instance=profile_instance)


    return render(request, 'seeker/profile_form.html', {
        'form': form
    })

@login_required(login_url='login_view')
def profile_view(request):
    seeker = Job_Seeker.objects.filter(user=request.user).first()

    if seeker is None:
        messages.error(request, "You are not registered as a job seeker.")
        return redirect('jobs')


    profile = Profile.objects.filter(user=seeker).first()

    if profile is None:
        messages.warning(request, "Profile not yet created!")
        return redirect('profile')  # redirect to profile creation page

    return render(request, "seeker/profile_view.html", {
        "profile": profile
    })

@login_required(login_url='login_view')
def apply_job(request,id):
    job = get_object_or_404(JobPost, id=id)

    seeker = get_object_or_404(Job_Seeker, user=request.user)

    if JobApplication.objects.filter(job=job, seeker=seeker).exists():
        messages.info(request, "You have already applied for this job.")
        return redirect('jobs')




    else:

        application = JobApplication()
        application.job = job
        application.seeker = seeker
        application.save()

        messages.success(request, "You successfully applied for the job!")
        return redirect('jobs')

@login_required(login_url='login_view')
def seeker_applied_jobs(request):
    seeker = get_object_or_404(Job_Seeker, user=request.user)
    applied_jobs = JobApplication.objects.filter(seeker=seeker)

    return render(request, "seeker/applied_jobs.html", {
        "applied_jobs": applied_jobs
    })

@login_required(login_url='login_view')
def seeker_shortlisted_jobs(request):
    seeker = get_object_or_404(Job_Seeker, user=request.user)
    shortlisted_jobs = ShortlistedCandidate.objects.filter(seeker=seeker).select_related('job')

    return render(request, "seeker/shortlisted_jobs.html", {
        "shortlisted_jobs": shortlisted_jobs
    })
