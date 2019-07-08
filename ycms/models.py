from django.conf import settings
from django.db import models





class event_details(models.Model):
	eDate = models.DateField(blank=False,)
	duration = models.IntegerField()
	vAddress = models.CharField(max_length=200, blank=True, null=True)
	eType = models.CharField(max_length=200)
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	contact = models.IntegerField()
	address = models.CharField(max_length=200)


	"""docstring for ClassName"""
	def __str__(self):
		return self.fname + " " + self.lname
	


class accounts(models.Model):
	username = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=50)


	"""docstring for ClassName"""
	def __str__(self):
		return self.username + " " + self.password
	

class login(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	"""docstring for ClassName"""
	def __str__(self):
		return self.username + " " + self.password
	
