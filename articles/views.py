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
