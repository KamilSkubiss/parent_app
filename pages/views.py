from random import sample

from django.shortcuts import render
from django.views.generic import TemplateView

from articles.models import Article


def home(request):
    articles = Article.objects.all()
    random_articles = sample(list(articles), min(len(articles), 3))
    return render(request, 'pages/home.html', {'articles': random_articles})
