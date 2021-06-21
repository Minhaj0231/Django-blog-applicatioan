from django.db import models
from django.shortcuts import render,  redirect
from .models import Post
from django.views.generic.edit import CreateView

from django.views.generic import  ListView 

class Home(ListView):

    template_name = "blog/index.html"
    model =  Post
    
    context_object_name = "posts"

    def get_queryset(self) :
        base_query =  super().get_queryset()
        data = base_query.order_by("-publish")[:3]
        return data
            

class ALL_Post(ListView):
    template_name = "blog/all_posts.html"
    model =  Post
    paginate_by = 3
    context_object_name = "posts"



# def all_post(request):
#     posts = Post.objects.all()

    

#     return render(request, "blog/all_posts.html",
#             {'posts':posts}
#             )


def post_detail(request,slug):

    post = Post.objects.get(slug=slug)

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id).distinct()

    print(similar_posts)

    return render(request, "blog/single_post.html",
            {'post':post,
             'similar_posts': similar_posts
            }
            )

class CreateBlog(CreateView):

    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog/blogform.html'
    success_url = ""

    def form_valid(self, form):
        data = form.save(commit=False)
        data.author = self.request.user
        data.save()
        
        return redirect("home_page")


