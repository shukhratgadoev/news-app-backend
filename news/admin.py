from django.contrib import admin
from .models import News
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author', 'date')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('id', 'title', 'description', 'author')
    
    
    
admin.site.register(News, NewsAdmin)