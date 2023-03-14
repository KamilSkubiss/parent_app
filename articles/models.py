from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.urls import reverse


MONTHS = (
    (0, '0 months'),
    (1, '1 months'),
    (2, '2 months'),
    (3, '3 months'),
    (4, '4 months'),
    (5, '5 months'),
    (5, '6 months'),
    (7, '7 months'),
    (8, '8 months'),
    (9, '9 months'),
    (10, '10 months'),
    (11, '11 months'),
    (12, '12 months'),
)


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='images/', blank=True)
    article_range = models.IntegerField(choices=MONTHS, null=False)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('article_detail', args=[str(self.id)])


# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
#     comment = models.CharField(max_length=140)
#     author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.comment

    # def get_absolute_url(self):
    #     return reverse('article_list')
from django.db import models

# Create your models here.
