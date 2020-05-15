from django.db import models

class Comment(models.Model):
	email			 = models.CharField(max_length=100)
	comments		 = models.CharField(max_length=800)
	created_at		 = models.DateTimeField(auto_now_add=True)
	updated_at		 = models.DateTimeField(auto_now=True)


class Meta:
	db_table = "comments"
