from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_recruiter =  models.BooleanField(default=False)
    is_seeker = models.BooleanField(default= False)


class Job_Seeker(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='job_seeker')
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=10)

class Recruiter(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='recruiter')
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.CharField(max_length=10)

class JobPost(models.Model):
    user = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='recruiter_name')
    JOB_TYPES = [('FT', 'Full-time'),('PT', 'Part-time'),('IN', 'Internship'),('CT', 'Contract'), ]

    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=2, choices=JOB_TYPES)
    salary = models.CharField(max_length=20)
    experience = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    application_deadline = models.DateField(blank=True)

class Profile(models.Model):
    user = models.ForeignKey(Job_Seeker, on_delete=models.CASCADE, related_name='profile')

    skills = models.TextField(blank=True)
    projects = models.TextField(blank=True)

    experience = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)



    tenth_school = models.CharField(max_length=150, blank=True)
    tenth_board = models.CharField(max_length=100, blank=True)
    tenth_year = models.CharField(max_length=10, blank=True)
    tenth_percentage = models.CharField(max_length=10, blank=True)

    twelfth_school = models.CharField(max_length=150, blank=True)
    twelfth_board = models.CharField(max_length=100, blank=True)
    twelfth_year = models.CharField(max_length=10, blank=True)
    twelfth_percentage = models.CharField(max_length=10, blank=True)

    bachelors_specialization= models.CharField(max_length=150, blank=True)
    bachelors_institute = models.CharField(max_length=100, blank=True)
    bachelors_year = models.CharField(max_length=10, blank=True)
    bachelors_cgpa = models.CharField(max_length=10, blank=True)

    masters_specialization = models.CharField(max_length=150, blank=True)
    masters_institute = models.CharField(max_length=100, blank=True)
    masters_year = models.CharField(max_length=10, blank=True)
    masters_cgpa = models.CharField(max_length=10, blank=True)



    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)

class JobApplication(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    seeker = models.ForeignKey(Job_Seeker, on_delete=models.CASCADE)







