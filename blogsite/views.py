from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import News, Articles, Category, NewsComment
from django.db.models import Q
from .forms import CommentForm

# Create your views here.
def NewsList(request):
	q=request.GET.get('q') if request.GET.get('q') != None else ''
	posts = News.objects.filter(
		Q(sub_sector__catgory__title__icontains=q)|
		Q(sub_sector__subcatgory__title__icontains=q)|
		Q(sub_sector__title__icontains=q)|
		Q(title__icontains=q)|
		Q(body__icontains=q)
		)
	cat = Category.objects.all()
	comments=NewsComment.objects.all()
	context={
	'posts':posts,
	'categories': cat,
	'comments': comments,
	'q':q,
	}
	return render(request, "blogsite/news.html", context)

def NewsDetail(request, slug, *args, **kwargs):
	news = get_object_or_404(News, slug=slug)
	comments = news.newscomment.filter(active=False)
	new_comment=None
	if request.method=='POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment=comment_form.save(commit=False)
			new_comment.post = news
			new_comment.user= request.user
			new_comment.save()
			return HttpResponseRedirect(reverse('blogsite:news-detail', kwargs={'slug':news.slug}))
	else:
		comment_form=CommentForm()
	context={
	'obj': news,
	'comments':comments,
	'comment_form': comment_form,
	'new_comment': new_comment,
	}
	return render(request, "blogsite/news_detail.html", context)


def ArticlesList(request):
	articles = Articles.objects.all()
	context={
	'articles':articles,
	}
	return render(request, "blogsite/articles.html", context)

def ArticleDetail(request, slug, *args, **kwargs):
	article = get_object_or_404(Articles, slug=slug)
	context ={
	'obj': article
	}
	return render(request, "blogsite/article_detail.html", context)


