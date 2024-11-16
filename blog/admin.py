from django.contrib import admin
from .models import Comment, Post, Tag

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = { "slug": ("title",)}
  list_display = ( "slug", "published_at" )

admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)