from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "autor",
        "body"
    )
    list_filter = (
        "title",
        "autor",
    )

admin.site.register(Post, PostAdmin)