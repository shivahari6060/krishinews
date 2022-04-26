from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserProfileForm

# Create your views here.
def users_profile(request):
	pass
def authors_profile(request):
	list_authors = UserProfile.objects.filter(role='A')
	context={
	'authors': list_authors
	}

	return render(request, 'profiles/authors_list.html', context)

def editors_profile(request):
	pass

def profile_detail(request):
	in_profile = get_object_or_404(UserProfile, user=request.user)
	form = UserProfileForm(instance=in_profile)

	context={
	'user':in_profile,
	'form': form,
	}
	return render(request, 'profiles/profile_detail.html', context)

def update_profile_detail(request):
	pass
