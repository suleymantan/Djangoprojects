from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("register/",views.register, name='register'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path("friends",views.friends,name='friends'),
    path("profile/<int:id>", views.profile, name = 'profile'),
    path("send_follow/<int:id>",views.send_follow, name='send-follow'),
    path("approved_follow/<int:id>",views.approve_follow, name='approved-follow'),
    path("rejete_follow/<int:id>",views.rejete_follow, name='rejete-follow'),
    
    
]
    
