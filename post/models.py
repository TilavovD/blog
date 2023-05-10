from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=32)
    slug = models.CharField(max_length=64)
    body = models.TextField(max_length=64)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
