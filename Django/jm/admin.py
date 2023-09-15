from django.contrib import admin
from . import models

# Register your models here.
# 관리자 페이지에서 Article 보고싶다..☆
admin.site.register(models.Article)