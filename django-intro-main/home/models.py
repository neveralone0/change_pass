from django.db import models


class Todo(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created = models.DateTimeField()
	owner = models.CharField(max_length=200)
	uid = models.IntegerField()
	parrent = models.IntegerField()
