
from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobHome, name='jobhome'),
    path('jobview/<str:id>',views.jobview,name='jobview'),
    path('postjob/',views.jobpost,name='postjob'),
    path('jobsearch/<str:btn>/<str:val>/<int:pagenumber>/',views.jobsearch,name='jobsearch'),
    path('jobsearch/',views.job_searchbtn,name="job_searchbtn")
  
]
    
