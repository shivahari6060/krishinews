from django.forms import ModelForm
from .models import *

#Now create forms
class CreateNewsForm(ModelForm):
	class Meta:
		model = News
		fields = ['title', 'body', 'categories', 'sub_categories', 'sub_sector']


class CommentForm(ModelForm):
    class Meta:
        model = NewsComment
        fields = ('email', 'body')