from django.db import models

class Account(models.Model):
	fullname		= models.CharField(max_length = 50)	
	username		= models.CharField(max_length = 300)
	email 			= models.CharField(max_length = 100, unique=True)
	password	     = models.CharField(max_length = 300)
	created_at 	     = models.DateTimeField(auto_now_add = True)
	updated_at 	     = models.DateTimeField(auto_now = True)


	class Meta:
		db_table = "accounts"
