from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.forms import RegisterForm,SearchForm
from articles.models import Article
from .models import Follow



@login_required
def index(request):
    followed_users = Follow.objects.filter(follower=request.user).values_list('following',flat=True)
    articles = Article.objects.filter(author__in=followed_users).order_by('-created_at')
    return render(request,'index.html',{'articles':articles})

def register(request):
    form=RegisterForm()
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request,"You have succesfully")
            return redirect ('login')
    else:
        return render(request, 'register.html',{'form':form})
        
def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in")
            return redirect('index')
        else:
            messages.error(request,"There was an error logging in Please try again ")
            return redirect('login')
    else:

        return render(request, "login.html")
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login')

User = get_user_model()
def friends(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query) |Q(last_name__icontains=query)).distinct()
    
    follow_requests = Follow.objects.filter(following = request.user,approved =False)
    follows = Follow.objects.filter(approved=True,following = request.user)
    followings = Follow.objects.filter(approved=True,follower=request.user )
    users = User.objects.filter(is_staff=False)
    context = {
        'users':users,
        'follow_requests':follow_requests,
        'follows':follows,
        'followings':followings,
        'form':form,
        'results':results,
    }
    print(results)
    return render(request,'friends.html',context)
@login_required
def profile(request,id):
    user = get_object_or_404(User, id=id)
    articles = Article.objects.filter(author=user)
    return render(request,'profile.html',{'user':user,'articles':articles})



def send_follow(request,id):
    follower = request.user
    following = get_object_or_404(User,id=id)
    if follower == following:
        return redirect('friends')
    if Follow.objects.filter(follower = follower,following=following).exists():
        return redirect('friends')
    Follow.objects.create(follower=follower,following=following)
    return redirect('friends')


def approve_follow(request, id):
    follow_request = get_object_or_404(Follow,id=id,following=request.user)
    follow_request.approved = True
    follow_request.save()
    return redirect('friends')


def rejete_follow(request,id):
    follow_request = get_object_or_404(Follow,id=id,following=request.user)
    follow_request.delete()
    return redirect('friends')




