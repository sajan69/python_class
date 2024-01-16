from django.contrib import admin
from .models import Category, BlogPost

class CategoryAdminModel(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)

class PostAdminModel(admin.ModelAdmin):
    list_display = ('title','author','category','created_at')
    list_filter = ('created_at',)
    list_editable = ('category',)

admin.site.register(Category, CategoryAdminModel)
admin.site.register(BlogPost, PostAdminModel)

