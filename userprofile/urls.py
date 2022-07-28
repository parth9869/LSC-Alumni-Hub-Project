""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   
    path('',views.viewProfile,name="viewprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
   
]