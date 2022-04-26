from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from profiles.models import Author

 

class BaseModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Category(BaseModel):
	title = models.CharField(max_length=150, blank=True, null=True)

	def __str__(self):
		return self.title

class Subcategory(BaseModel):
	catgory= models.ForeignKey(Category, on_delete= models.CASCADE, blank=True, null=True)
	title = models.CharField(max_length=150, blank=True, null=True)

	def __str__(self):
		return self.title

class Subsector(BaseModel):
	catgory= models.ForeignKey(Category, on_delete= models.CASCADE, blank=True, null=True)
	subcatgory = models.ForeignKey(Subcategory, on_delete= models.CASCADE, blank=True, null=True) 
	title = models.CharField(max_length=150, blank=True, null=True)

	def __str__(self):
		return self.title

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=350, blank=True, null=True)
	slug = models.SlugField(unique=True, null=True, blank=True)
	categories = models.CharField(max_length=150, blank=True, null=True)
	sub_categories = models.CharField(max_length=150, blank=True, null=True)
	sub_sector = models.ForeignKey(Subsector, on_delete=models.SET_NULL, blank=True, null=True)
	body = models.TextField(max_length=1000, blank=True, null=True)
	published_date= models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	author= models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True, related_name='news_author')
	likes = models.IntegerField(blank=True, null=True)
	comments = models.IntegerField(blank=True, null=True)
	publish = models.BooleanField(default=False)
	pinned = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-published_date"]

	def get_absolute_url(self):
		return "%s/" %(self.slug)


#creating slug for News
def create_news_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.title)
	qs = News.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s"%(slug, qs.first().id)
		return create_news_slug(instance, new_slug=new_slug)
	return slug

#now opening pre_save receiver
def pre_save_news_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_news_slug(instance)

pre_save.connect(pre_save_news_receiver, sender=News)



class Articles(models.Model):
	title = models.CharField(max_length=350, blank=True, null=True)
	slug = models.SlugField(unique=True, null=True, blank=True)
	categories = models.CharField(max_length=150, blank=True, null=True)
	sub_categories = models.CharField(max_length=150, blank=True, null=True)
	sub_sector = models.CharField(max_length=150, blank=True, null=True)
	body = models.TextField(max_length=1000, blank=True, null=True)
	published_date= models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	author= models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True, related_name='aricle_author')
	likes = models.IntegerField(blank=True, null=True)
	comments = models.IntegerField(blank=True, null=True)
	publish = models.BooleanField(default=False)
	pinned = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering =['-published_date']

	def get_absolute_url(self):
		return "%s" %(self.slug)


#creating slug for Articles
def create_articles_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.title)
	qs = Articles.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s"%(slug, qs.first().id)
		return create_articles_slug(instance, new_slug=new_slug)
	return slug

#now opening pre_save receiver
def pre_save_articles_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_news_slug(instance)

pre_save.connect(pre_save_articles_receiver, sender=Articles)


class ArticleComment(models.Model):
    post = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='articlescomment')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class NewsComment(models.Model):
    post = models.ForeignKey(News,on_delete=models.CASCADE,related_name='newscomment')
    user= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='commenter')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)


class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    last_name =models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Contact message  {} by {}'.format(self.body, self.first_name)