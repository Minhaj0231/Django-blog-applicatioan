from django.urls import path

from . import views 

urlpatterns = [
    path("", views.Home.as_view(), name="home_page"),
    path("posts", views.ALL_Post.as_view(), name="all_post"),
    path("posts/<slug:slug>", views.post_detail, name="post_detail"),
    path("postForm/", views.CreateBlog.as_view(), name="post_form")
    
]