from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Article


class CustomerArticlesAdmin(UserAdmin):
    model = Article
    list_display = ['title', 'body', 'date', '']


admin.site.register(Article)
