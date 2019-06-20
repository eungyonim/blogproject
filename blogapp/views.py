from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# model에서 Blog 클래스를 가져올게욤
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

#blog는 블로그에서 가져온 객체가 들어갑니다.
#home.html의 요청이 왔을 때 blogs의 key:values를 같이 내준다
#딕셔너리로 담으면 key사용 시 그 객체를 사용할 수가 잇다

def detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog() 
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/blog/'+str(blog.id))
    