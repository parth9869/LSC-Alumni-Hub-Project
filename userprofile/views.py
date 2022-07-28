from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from user.models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.
def educationList(university,degree,program,startdate,enddate,description):
    # this funcation create list of dicationary of education.
    education=[]
    for i in range(0,len(university)):
        temp={}
        temp['university']=university[i].title()
        temp['degree']=degree[i].title()
        temp['program']=program[i].title()
        temp['startdate']=startdate[i]
        if enddate[i] == 'Present':
            temp['enddate']=''
        else:
            temp['enddate']=enddate[i]
        temp['description']=description[i].capitalize()
        education.append(temp)
    return education
    
def workExperienceList(position,company,startdate,enddate,description):
     # this funcation create list of dicationary of work experience.
     work=[]
     for i in range(0,len(position)):
        temp={}
        temp['position']=position[i].title()
        temp['company']=company[i].title()
        temp['startdate']=startdate[i]
        if enddate[i] == 'Present':
            temp['enddate']=''
        else:
            temp['enddate']=enddate[i]
        temp['description']=description[i].capitalize()
        work.append(temp)
     return work

def publicationList(title,journalname,date,url):
    # this funcation create list of dicationary of Publications.
    publication=[]
    for i in range(0,len(title)):
        temp={}
        temp['title']=title[i].title()
        temp['journal']=journalname[i].title()
        temp['date']=date[i]
        temp['url']=url[i]
        publication.append(temp)
    return publication

def certificationList(title,institute,date,url):
    # this funcation create list of dicationary of certifications.
    certification=[]
    for i in range(0,len(title)):
        temp={}
        temp['title']=title[i].title()
        temp['institute']=institute[i].title()
        temp['date']=date[i]
        temp['url']=url[i]
        certification.append(temp)
    return certification


@login_required(login_url="/")
def editprofile(request):
    profile=request.user
    if request.method=='POST':
       
        profile.firstname=request.POST['firstName'].capitalize()
        profile.lastname=request.POST['lastName'].capitalize()
        profile.email=request.POST['email']
        profile.usertype=request.POST['userType']

        if profile.usertype=='Student' or profile.usertype=='Alumni':
            profile.programname=request.POST['programName'].capitalize()
        else :
            profile.programname=''
        if profile.usertype=='Alumni':
            profile.passingyear=request.POST['passingYear']
        else:
            profile.passingyear=0000
        profile.mobile=request.POST['mobileNumber']
        profile.city=request.POST['city'].title()
        profile.province=request.POST['province'].title()
        profile.country=request.POST['country'].title()
        profile.about=request.POST['about'].capitalize()
        
        profile.educations=educationList(university=request.POST.getlist('university[]'),
        degree=request.POST.getlist('degree[]'),
        program=request.POST.getlist('program[]'),
        startdate=request.POST.getlist('startDate[]'),
        enddate=request.POST.getlist('endDate[]'),
        description=request.POST.getlist('educationDescription[]')
        
        )

        profile.workexperiences= workExperienceList(
            position=request.POST.getlist('position[]'),
            company=request.POST.getlist('company[]'),
            startdate=request.POST.getlist('startDateWork[]'),
            enddate=request.POST.getlist('endDateWork[]'),
            description=request.POST.getlist('workDescription[]')
            )

        profile.publications=publicationList(
            title=request.POST.getlist('publicationTitle[]'),
            journalname=request.POST.getlist('publicationJournal[]'),
            date=request.POST.getlist('publicationDate[]'),
            url=request.POST.getlist('publicationUrl[]'),
        )

        profile.certifications=certificationList(
            title=request.POST.getlist('certificateTitle[]'),
            institute=request.POST.getlist('certificateInstitute[]'),
            date=request.POST.getlist('certificateDate[]'),
            url=request.POST.getlist('certificateUrl[]'),
        )

        profile.personalwebsite=request.POST['personalWebsite']
        profile.github=request.POST['github']
        profile.linkedin=request.POST['linkedin']
        if request.FILES:
             profile.profileimage=request.FILES['profileImage'] 
        
        
        try:
             profile.save()
             return redirect('../../userprofile')
        except:
            
            return render(request,'editProfile.html',{'profile':profile})
       
    else:
        return render(request,'editProfile.html',{'profile':profile})



@login_required(login_url="/")
def viewProfile(request):

    # render for profile page.
    return render(request,"profile.html")