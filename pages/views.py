from django.shortcuts import render
from django.views.generic import TemplateView
from articles.models import Article
import random


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


def carousel(request):
    all_articles = Article.objects.all()
    article_list = list(all_articles)
    random.shuffle(article_list)
    context = {
        'first_article_name': article_list[0].title,
        'first_article_image': article_list[0].article_image,
        'second_article_name': article_list[1].title,
        'second_article_image': article_list[1].article_image,
        'third_article_name': article_list[2].title,
    }
    return render(request, 'pages/home.html', context)
