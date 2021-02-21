from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'language', 'tonality')
    list_display_links = ('id',)
    search_fields = ('id', 'text')
    list_filter = ('language', 'tonality')


admin.site.register(Article, ArticleAdmin)
