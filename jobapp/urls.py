from django.urls import path

from jobapp import views, recruiter_views, seeker_views

urlpatterns =[
path('',views.home,name='home'),
    path('login',views.loginv,name='login'),
    path('index',views.index,name='index'),
    path('seeker_add',views.seeker_add,name='seeker_add'),
    path('recruiter_add',views.recruiter_add,name='recruiter_add'),
    path('admin',views.admin_base,name='admin'),
    path('seeker',views.seeker_base,name='seeker'),
    path('recruiter',views.recruiter_base,name='recruiter'),
    path('login_view',views.login_view,name='login_view'),

    #admin
    path('view_seeker',views.view_seeker,name='view_seeker'),
    path('view_recruiter',views.view_recruiter,name='view_recruiter'),
    path('delete_seeker/<int:id>/', views.delete_seeker, name='delete_seeker'),
    path('delete_recruiter/<int:id>/', views.delete_recruiter, name='delete_recruiter'),
path('update_seeker/<int:id>/', views.update_seeker, name='update_seeker'),
path('update_recruiter/<int:id>/', views.update_recruiter, name='update_recruiter'),

 path('jobform',views.job_form_upload,name='jobform'),
    path('joblist',recruiter_views.joblist,name='joblist'),

    #seeker
    path('jobs',seeker_views.jobs,name='jobs'),
path('job_details/<int:id>/', seeker_views.job_details, name='job_details'),
    path('profile',seeker_views.profile,name='profile'),
    path('profile_view/<int:id>/',seeker_views.profile_view,name='profile_view')





]