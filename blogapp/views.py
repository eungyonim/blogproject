from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import BlogPost
# model에서 Blog 클래스를 가져올게욤
# Create your views here.

def home(request):
    blogs = Blog.objects 
    blog_list=Blog.objects.all() #블로그 모든 글들을 대상으로
    paginator = Paginator(blog_list,3) #블로그 객체 세 개를 한 페이지로 자르기
    page = request.GET.get('page') #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    posts = paginator.get_page(page) #request된 페이지를 얻어온 뒤 return 해 준다
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

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

def blogpost(request):
	if request.method == 'POST':
		# POST방식으로 요청이 들어왔을 때 실행할 코드 - form에 입력받은 데이터를 저장하기
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
		# GET방식으로 요청이 들어왔을 때 실행할 코드 - form을 보여주기
        form = BlogPost()
        return render(request,'new.html',{'form':form})