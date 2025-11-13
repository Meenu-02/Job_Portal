from django.contrib import admin

from jobapp import models

# Register your models here.
admin.site.register(models.Login)

admin.site.register(models.Job_Seeker)

admin.site.register(models.Recruiter)