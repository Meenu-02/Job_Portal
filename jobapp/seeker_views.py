from django.shortcuts import render, redirect

from jobapp.forms import ProfileForm
from jobapp.models import JobPost, Profile, Job_Seeker


def jobs(request):
    data=JobPost.objects.all()
    return render(request, 'seeker/jobs.html', {'jobs': data})

def job_details(request,id):
    data=JobPost.objects.get(id=id)
    return render(request,'seeker/job_details.html',{'details':data})

def profile(request):

    data=request.user
    profile_data=Profile.objects.get(Job_Seeker,user=data)




    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            object = form.save(commit=False)
            object.user = profile_data
            object.save()

            return redirect('profile_view')
    else:
        form = ProfileForm()
    return render(request, 'seeker/profile_form.html', {
        'form': form
    })

def profile_view(request,id):
    data = Profile.objects.get(id=id)
    return render(request, 'seeker/profile_view.html', {'view': data})


