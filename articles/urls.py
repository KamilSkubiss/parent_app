from django.urls import path

from articles.views import ArticleView0


urlpatterns = [
    path('0/', ArticleView0.as_view(), name='article_view0')
]
