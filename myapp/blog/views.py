from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
# Create your views here.
posts=[
        {'title':"post 1",'content':"Content 0f post 1", 'area':"Sports",'post_id':1},
        {'title':"post 2",'content':"Content 0f post 2", 'area':"movies",'post_id':2},
        {'title':"post 3",'content':"Content 0f post 3", 'area':"Science",'post_id':3},
        {'title':"post 4",'content':"Content 0f post 4", 'area':"Development",'post_id':4},
        {'title':"post 5",'content':"Content 0f post 5", 'area':"culture",'post_id':5},
        {'title':"post 6",'content':"Content 0f post 6", 'area':"History",'post_id':6}
        
    ]
def index(request):
    blog_title="Today's Post"
    return render(request,"index.html", {'blog_title':blog_title , 'posts':posts})

def post(request, post_id):
    post=next((item for item in posts if item['post_id'] == post_id),None)
    # logger=logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')
    return render(request,"details.html",{'post':post})

def old_url_redirect(request):
     return redirect(reverse("blog:new_page_url")) 

def new_url_view(request):
    return HttpResponse("Redirected to new url")