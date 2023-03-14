from django.views.generic import ListView

from .models import Article


class ArticleView0(ListView):
    model = Article
    template_name = 'articles/0months.html'
