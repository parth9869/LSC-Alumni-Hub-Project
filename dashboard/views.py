from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from djongo.models import ObjectIdField
from user.models import CustomUser
from djongo.models.fields import GenericObjectIdField
# Create your views here.

@login_required(login_url='/')
def dashboard(request):
    # render dashboard.html file from templates folder of application
    return render(request,"Dashboard.html")
