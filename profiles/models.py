from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.core.validators import RegexValidator

# Create your models here.



class UserProfile(models.Model):
	phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
	user= models.OneToOneField(User, on_delete= models.CASCADE, blank=True, null=True)
	first_name = models.CharField(max_length= 100, blank=True, null=True)
	last_name = models. CharField(max_length= 100, blank=True, null=True)
	phone = models.CharField(max_length=15, validators=[phoneNumberRegex], unique=True, null=True, blank=True)
	address = models.CharField(max_length=350, blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)



	def __str__(self):
		return str(self.user)

		
def create_userprofile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_userprofile, sender=User)

def update_userprofile(sender, instance, created, **kwargs):
	if created == False:
		instance.userprofile.save()

post_save.connect(update_userprofile, sender=User)


class Author(models.Model):
	education = models.CharField(max_length=200, blank=True, null=True)
	major_field = models.CharField(max_length=200, blank=True, null=True)
	author_rating = models.FloatField(blank=True, null=True)
	editor_rating = models.FloatField(blank=True, null=True)
	phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
	author= models.OneToOneField(UserProfile, on_delete= models.CASCADE, blank=True, null=True)
	

	def __str__(self):
		return(str(self.author))
		