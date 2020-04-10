from django.contrib import admin
from .models import UserProfile, UserProfileFeedItem
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserProfileFeedItem)
