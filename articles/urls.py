from django.urls import path

from articles.views import ArticleView0, CommentCreateView, ArticleDetailView, ArticleView1, ArticleView2, ArticleView3, \
    ArticleView4, ArticleView5, ArticleView6, ArticleView7, ArticleView8, ArticleView9, ArticleView10, ArticleView11, \
    ArticleView12

urlpatterns = [
    path('0/', ArticleView0.as_view(), name='article_view0'),
    path('1/', ArticleView1.as_view(), name='article_view1'),
    path('2/', ArticleView2.as_view(), name='article_view2'),
    path('3/', ArticleView3.as_view(), name='article_view3'),
    path('4/', ArticleView4.as_view(), name='article_view4'),
    path('5/', ArticleView5.as_view(), name='article_view5'),
    path('6/', ArticleView6.as_view(), name='article_view6'),
    path('7/', ArticleView7.as_view(), name='article_view7'),
    path('8/', ArticleView8.as_view(), name='article_view8'),
    path('9/', ArticleView9.as_view(), name='article_view9'),
    path('10/', ArticleView10.as_view(), name='article_view10'),
    path('11/', ArticleView11.as_view(), name='article_view11'),
    path('12/', ArticleView12.as_view(), name='article_view12'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail_view'),
    path('<int:article_pk>/comment/', CommentCreateView.as_view(), name='comment_new'),

]
