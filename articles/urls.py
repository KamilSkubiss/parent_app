from django.urls import path

from articles.views import ArticleView0, CommentCreateView, ArticleDetailView

urlpatterns = [
    path('0/', ArticleView0.as_view(), name='article_view0'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail_view'),
    path('<int:article_pk>/comment/', CommentCreateView.as_view(), name='comment_new'),

]
