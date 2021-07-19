from blog.models import Author, Coment, Post, Tag
from django.contrib import admin

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", "image",)
    list_filter = ("author", "tag", "date",)
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Coment, CommentAdmin)
admin.site.register(Tag)