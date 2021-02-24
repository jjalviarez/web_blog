from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created','modified')

class ProductAdmin(admin.ModelAdmin):
    readonly_fields= ('created','modified')

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
