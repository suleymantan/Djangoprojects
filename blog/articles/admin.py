from django.contrib import admin
from .models import Article,Comment



class AdminArticle(admin.ModelAdmin):
    list_display =['title','author','created_at','image']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article,AdminArticle)
admin.site.register(Comment)
