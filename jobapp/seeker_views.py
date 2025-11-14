from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from jobapp.forms import ProfileForm
from jobapp.models import JobPost, Profile, Job_Seeker, JobApplication


def jobs(request):
    data=JobPost.objects.all()
    return render(request, 'seeker/jobs.html', {'jobs': data})

def job_details(request,id):
    data=JobPost.objects.get(id=id)
    return render(request,'seeker/job_details.html',{'details':data})

def profile(request):
    seeker = get_object_or_404(Job_Seeker, user=request.user)

    # check if profile exists, else create new
    profile_instance, created = Profile.objects.get_or_create(user=seeker)




    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile_instance)

        if form.is_valid():
            form.save()
            return redirect('jobs')
    else:
             form = ProfileForm(instance=profile_instance)


    return render(request, 'seeker/profile_form.html', {
        'form': form
    })

def profile_view(request):

    # Get Job_Seeker linked to logged-in Login user
    seeker = get_object_or_404(Job_Seeker, user=request.user)

    # Get Profile linked to Job_Seeker
    profile = get_object_or_404(Profile, user=seeker)

    return render(request, 'seeker/profile_view.html', {
        'profile': profile
    })


def apply_job(request,id):
    job = get_object_or_404(JobPost, id=id)

    # get the logged-in user's seeker profile
    seeker = get_object_or_404(Job_Seeker, user=request.user)

    # check if already applied
    if JobApplication.objects.filter(job=job, seeker=seeker).exists():
        messages.info(request, "You have already applied for this job.")
        return redirect('jobs')




    else:
        # create application
        application = JobApplication()
        application.job = job
        application.seeker = seeker
        application.save()

        messages.success(request, "You successfully applied for the job!")
        return redirect('jobs')