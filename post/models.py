from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=32)
	slug = models.CharField(max_length=64)
	body = models.TextField(max_length=64)
	
	def __str__(self):
		return self.title
