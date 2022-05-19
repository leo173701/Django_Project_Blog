from django.contrib import admin

# Register your models here.
from .models import Article


admin.site.register(Article)      #必须增加这一行，否则进入后台什么都没有