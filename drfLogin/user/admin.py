from django.contrib import admin
from user.models import User

admin.site.register(User) # 기본 ModelAdmin으로 등록