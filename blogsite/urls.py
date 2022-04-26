from django.urls import path
from .views import *

app_name='blogsite'

urlpatterns = [
    path('news/', NewsList, name='news'),
    path('news/<slug:slug>/', NewsDetail, name='news-detail'),
    path('articles/', ArticlesList, name='articles'),
    path('articles/<slug:slug>/', ArticleDetail, name='articles-detail'),
]