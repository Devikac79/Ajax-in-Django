from app.views import likePost
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Post)
admin.site.register(Like)