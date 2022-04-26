from django.urls import path
from .views import *

app_name='profiles'

urlpatterns = [
    path('authors/', authors_profile, name='authors-list'),
    path('detail/', profile_detail, name='profile-detail'),
]