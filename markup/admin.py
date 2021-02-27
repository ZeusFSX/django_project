from django.contrib import admin
from .models import Article, Entity


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'language', 'tonality')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'text')
    list_filter = ('language', 'tonality')


class EntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'offset', 'length', 'text', 'type_entity')
    list_display_links = ('id', 'text', 'type_entity')
    search_fields = ('id', 'text')
    list_filter = ('type_entity', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Entity, EntityAdmin)
