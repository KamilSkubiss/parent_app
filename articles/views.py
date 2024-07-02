from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse

from .models import Article, Comment


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    login_url = 'login'


class ArticleView0(ListView):
    model = Article
    template_name = 'articles/0months.html'
    context_object_name = 'article'


class ArticleView1(ListView):
    model = Article
    template_name = 'articles/1months.html'
    context_object_name = 'article'


class ArticleView2(ListView):
    model = Article
    template_name = 'articles/2months.html'
    context_object_name = 'article'


class ArticleView3(ListView):
    model = Article
    template_name = 'articles/3months.html'
    context_object_name = 'article'


class ArticleView4(ListView):
    model = Article
    template_name = 'articles/4months.html'
    context_object_name = 'article'


class ArticleView5(ListView):
    model = Article
    template_name = 'articles/5months.html'
    context_object_name = 'article'


class ArticleView6(ListView):
    model = Article
    template_name = 'articles/6months.html'
    context_object_name = 'article'


class ArticleView7(ListView):
    model = Article
    template_name = 'articles/7months.html'
    context_object_name = 'article'


class ArticleView8(ListView):
    model = Article
    template_name = 'articles/8months.html'
    context_object_name = 'article'


class ArticleView9(ListView):
    model = Article
    template_name = 'articles/9months.html'
    context_object_name = 'article'


class ArticleView10(ListView):
    model = Article
    template_name = 'articles/10months.html'
    context_object_name = 'article'


class ArticleView11(ListView):
    model = Article
    template_name = 'articles/11months.html'
    context_object_name = 'article'


class ArticleView12(ListView):
    model = Article
    template_name = 'articles/12months.html'
    context_object_name = 'article'


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'articles/comment_new.html'
    fields = ('comment',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['article_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_view', kwargs={'pk': self.kwargs['article_pk']})
