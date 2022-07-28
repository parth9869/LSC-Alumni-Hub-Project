from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Userlogin, name='login'),
    path('register/',views.register,name="register"),
    path('logout/',views.Userlogout,name="logout"),
  
]
    
