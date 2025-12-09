from django.contrib import admin

from .models import BlogPost, Category

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'author')
    search_fields = ('title', 'content', 'tag')
    prepopulated_fields = {'title': ('title',)}
    ordering = ('-created_at',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
