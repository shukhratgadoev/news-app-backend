from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author', 'date')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('id', 'title', 'description', 'author')
    
    
    
admin.site.register(Article, ArticleAdmin)
# Register your models here.
