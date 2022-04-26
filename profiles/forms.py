from django.forms import ModelForm
from .models import UserProfile


#Now make forms
class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields =['user','first_name', 'last_name',  'phone', 'address']