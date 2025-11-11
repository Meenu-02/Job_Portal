from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import render, redirect

from jobapp.forms import LoginRegister, SeekerRegister, RecruiterRegister
from jobapp.models import Recruiter, Seeker


# Create your views here.

def home(request):
    return render(request,'home.html')

def loginv(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def seeker_add(request):
    form1=LoginRegister()
    form2=SeekerRegister()

    if request.method == 'POST':
        form3= LoginRegister(request.POST)
        form4= SeekerRegister(request.POST)
        if form3.is_valid() and form4.is_valid():
            a= form3.save(commit=False)
            a.is_seeker = True
            a.save()
            user1 = form4.save(commit=False)
            user1.user = a
            user1.save()

            return redirect('home')
    return render(request,'seeker_registration.html',{'form1':form1,'form2':form2})

def recruiter_add(request):
    form1= LoginRegister()
    form2= RecruiterRegister()


    if request.method == 'POST':
        form3 = LoginRegister(request.POST)
        form4= RecruiterRegister(request.POST)



        if form3.is_valid() and form4.is_valid():
            a = form3.save(commit=False)
            a.is_seller = True
            a.save()


            user1 = form4.save(commit=False)
            user1.user = a
            user1.save()

            return redirect('home')


    return render(request,'recruiter_registration.html',{'form1':form1,'form2':form2})

def seeker_base(request):
    return render(request,'seeker/seeker.html')

def recruiter_base(request):
    return render(request,'recruiter/recruiter.html')

def admin_base(request):
    return render(request,'admin/admin.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')

        password = request.POST.get('pass')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('home')  #url name
            elif user.is_seeker:
                return redirect('home')
            elif user.is_recruiter:
                return redirect('home')

        else:
            messages.info(request,'Invalid Credentials')

    return render(request,'login.html')


def view_seeker(request):
    data= Seeker.objects.all()
    return render(request,'admin/seeker_view.html',{'view_seeker':data})

def view_recruiter(request):
    data= Recruiter.objects.all()
    return render(request,'admin/recruiter_view.html',{'view_recruiter':data})

def delete_seeker(request,id):
    data=Seeker.objects.get(id=id)

    data.delete()
    return redirect('view_seeker')


def delete_recruiter(request,id):
    data=Recruiter.objects.get(id=id)
    data.delete()
    return redirect('view_recruiter')

def update_seeker(request,id):
    data=Seeker.objects.get(id=id)
    form=SeekerRegister(instance=data) #form will be with data


    if request.method =='POST':
         details = SeekerRegister(request.POST,instance=data)
         if details.is_valid():
             details.save()
             return  redirect('view_seeker')
    return render(request,'admin/seeker_update.html',{'update':form})

def update_recruiter(request,id):
    data=Recruiter.objects.get(id=id)
    form=RecruiterRegister(instance=data) #form will be with data


    if request.method =='POST':
         details = RecruiterRegister(request.POST,instance=data)
         if details.is_valid():
             details.save()
             return  redirect('view_recruiter')
    return render(request,'admin/recruiter_update.html',{'update':form})






