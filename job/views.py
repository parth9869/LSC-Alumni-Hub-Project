from re import X
from turtle import title
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import postForm
from .models import jobs
from user.models import CustomUser
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def jobHome(request):
    recentjobs=jobs.objects.all().order_by('-date')
    counts={}
    counts['Marketing']=jobs.objects.filter(category='Marketing').count()
    counts['Customer_Service']=jobs.objects.filter(category='Customer Service').count()
    counts['Human_Resource']=jobs.objects.filter(category='Human Resource').count()
    counts['Project_Management']=jobs.objects.filter(category='Project Management').count()
    counts['Business_Development']=jobs.objects.filter(category='Business Development').count()
    counts['Sales_Communication']=jobs.objects.filter(category='Sales and Communication').count()
    counts['Design_Creative']=jobs.objects.filter(category='Design & Creative').count()
    counts['Information_Technology']=jobs.objects.filter(category='Information Technology').count()
    
       
    return render(request,'jobhome.html',{"recentjobs":recentjobs,"counts":counts})

@login_required(login_url='/')
def job_searchbtn(request):
    if request.method=='GET':
        search_fileter={}
        urlstring=''
        pagenumber=request.GET.get('page', 1)
        if request.GET['category']:
            search_fileter['category']=  request.GET['category']
            urlstring= urlstring+'&category='+request.GET['category']
        if request.GET['location']:
            search_fileter['location']=request.GET['location']
            urlstring= urlstring+'&location='+request.GET['location']
        if request.GET['title']:
            search_fileter['title']=request.GET['title']
            urlstring= urlstring+'&title='+request.GET['title']
       
        resultset=jobs.objects.filter(**search_fileter).order_by('-date')
        if resultset:
            paginator=Paginator(resultset,2)
            
            finalresultset=paginator.get_page(pagenumber)
            return render(request,'jobsearch.html',{"jobs":finalresultset,"btn":"search","url":urlstring})
        else:
            return render(request,'jobsearch.html',{"jobs":"","btn":"search","url":urlstring})
     
    
@login_required(login_url='/')
def jobsearch(request,btn,val,pagenumber):
    if btn=="recent":

        resultset=jobs.objects.all().order_by('-date')
        if resultset:
            paginator=Paginator(resultset,2)
            
            finalresultset=paginator.get_page(pagenumber)
            return render(request,'jobsearch.html',{"jobs":finalresultset,"btn":btn,"val":val})
        else:
             return render(request,'jobsearch.html',{"jobs":'',"btn":btn,"val":val})


    elif btn=="category":
        resultset=jobs.objects.filter(category=val).order_by('-date')
        if resultset:
            paginator=Paginator(resultset,2)
            
            finalresultset=paginator.get_page(pagenumber)
            return render(request,'jobsearch.html',{"jobs":finalresultset,"btn":btn,"val":val})
        else:
             return render(request,'jobsearch.html',{"jobs":'',"btn":btn,"val":val})


@login_required(login_url='/')
def jobview(request,id):
    resultset=jobs.objects.get(_id=id)
    jobposterdetails=CustomUser.objects.get(_id=resultset.postby)
    return render(request,'jobview.html',{'job':resultset,'jobposterdetails':jobposterdetails})




@login_required(login_url='/')
def jobpost(request):
    if request.method=='POST':
        form=postForm(request.POST)
        form.postby=request.user._id
        
        
        if form.is_valid():
            form.save()
            return redirect("../")
        else:
            
            return render(request,'postjob.html',{'form':form})
    else:
        form=postForm(initial={'postby':request.user._id})
        return render(request,'postjob.html',{'form':form})



