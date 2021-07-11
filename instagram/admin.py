from django.contrib import admin
from .models import Profile, Images, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Images)
admin.site.register(Comment)