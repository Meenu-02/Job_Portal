from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_recruiter =  models.BooleanField(default=False)
    is_seeker = models.BooleanField(default= False)


class Seeker(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='seeker')
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
    # user = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='recruiter_name')
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
