from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish" )
    list_filter = ("author", "publish")
    search_fields = ("title", "content")
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = "publish"
    ordering = ("publish",)



admin.site.register(Post, PostAdmin)
