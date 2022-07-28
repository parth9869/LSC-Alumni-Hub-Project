from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
from .forms import UserCreationForm,UserLoginForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect


def Userlogin(request):
  # handle request for and from login.html page.
  if request.method=="POST":
   
    form=UserLoginForm(request.POST)
    if form.is_valid():
        # if form is valid and all data verified. then authenticate() function user to authenticate and session object is using login funcation.
        password=form.cleaned_data.get('password')
        email1=form.cleaned_data.get('email')
        user=authenticate(email=email1,password=password)
        login(request,user)
        next= request.POST.get("next", None)
       
       # if next parameter of request is set then after successful login,system redirct user to page indicate by next parameter. 
        if next:
          return redirect(next)
        else:
          return redirect("dashboard/")
    else:
      # when there is error in submited form ,following will executed
      contx={'form':form}
      return render(request,"registration/login.html",contx)
  else:
     #if no data sent through requst then following section will execute. this section will display login page with emaplty login form.
      form=UserLoginForm()
      contx={'form':form}
      return render(request,"registration/login.html",contx)


@login_required(login_url="/")
def Userlogout(request):
  # when user click on logout. it will terminate session and redirect user to login page.
  logout(request)
  return redirect('/')
  
def register(request):
  
  if request.method=='POST':
    #when user submit registration from.
      form=UserCreationForm(request.POST)
      
      if form.is_valid():
        # form has valid data.
          form.save()
          form=UserCreationForm()
          contx={'form':form,'message':'usercreated'}
          return render(request,'registration/registration.html',contx)
      else :
         # form has error in data. this will render submitted from with error message displayed.
        contx={'form':form}
        
        return render(request,'registration/registration.html',contx)
        

           
  else:     
        form=UserCreationForm()
        contx={'form':form}
        return render(request,'registration/registration.html',contx)



