
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):

    default = "default"

    title = models.CharField(max_length=150, default=default,unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts",  default = "default" )
    content = models.TextField(default = "default", validators=[MinLengthValidator(6)])
    slug = models.SlugField(default = "default", null=False)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = "uploads", null=True, blank=True)
    tags = TaggableManager()

    class Meta: 
        ordering = ('-publish',)

    
    def get_absulate_url(self):
        return reverse('post_detail',kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):

        self.slug = slugify(self.title)
        super().save(*args, **kwargs)




    def __str__(self):
        return self.title


    