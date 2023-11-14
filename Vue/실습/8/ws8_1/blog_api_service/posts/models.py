from django.db import models

# Create your models here.
class Category(models.model):
    name = models.CharField(max_length=250)

class Post(models.model):
    category = 
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.model):
    post = 
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    