from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created','modified')


class PostAdmin(admin.ModelAdmin):
    readonly_fields= ('created','modified')

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
