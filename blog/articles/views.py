from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import ArticleForm,CommentForm
from .models import Article,Comment


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request, "create_articles.html",{'form':form})


def read_article(request,slug):
    article_read = Article.objects.select_related('author').get(slug=slug)
    
    return render(request,'read_article.html',{'article_read':article_read})
  
def comment(request,slug):
    article_comment = Article.objects.select_related('author').get(slug=slug)
    comments = Comment.objects.filter(article=article_comment).order_by('-created_at')
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article_comment
            comment.author = request.user
            comment.save()
            return redirect ('comment',slug=slug)
    else:
        form =CommentForm

    context = {
        'article_comment':article_comment,
        'form':form,
        'comments':comments,
    }
    
    return render(request,'comment.html',context)     

def article_update(request,id):
    article = Article.objects.get(id=id)
    if request.method =='POST':
        form = ArticleForm(request.POST,request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article
    }

    return render(request, 'article_update.html',context)

def article_delete(request,id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('profile',id=id)

