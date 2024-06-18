from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    blog_title="Today's Post"
    posts=[
        {'title':"post 1",'content':"Content 0f post 1", 'area':"Sports"},
        {'title':"post 2",'content':"Content 0f post 2", 'area':"movies"},
        {'title':"post 3",'content':"Content 0f post 3", 'area':"Science"},
        {'title':"post 4",'content':"Content 0f post 4", 'area':"Development"},
        {'title':"post 5",'content':"Content 0f post 5", 'area':"culture"},
        {'title':"post 6",'content':"Content 0f post 6", 'area':"History"}
        
    ]
    return render(request,"index.html", {'blog_title':blog_title , 'posts':posts})

def post(request, post_id):
    return render(request,"details.html")

def old_url_redirect(request):
     return redirect(reverse("blog:new_page_url")) 

def new_url_view(request):
    return HttpResponse("Redirected to new url")