from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),  
    path('post/<int:post_id>', views.post, name="post"),
    path('new_post_url_1233', views.new_url_view, name="new_page_url"),
    path('old_url', views.old_url_redirect, name="old_url")

]
