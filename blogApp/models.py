from django.db import models
from datetime import datetime
from django.shortcuts import reverse
from django.contrib.auth.models import User

# import smtplib 

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='Profile')

	def __str__(self):
		return self.user.username


class Blog(models.Model):
	title = models.CharField(max_length=800)
	brief = models.CharField(max_length=2500)
	body = models.TextField()
	image = models.ImageField(upload_to='Blog_Img', null=True, blank=True)
	slug = models.CharField(max_length=100, unique=True)
	date = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("blogApp:blogdetail", kwargs={'slug':self.slug})

	class Meta:
		ordering = ['-date']


class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=300)
	phone = models.IntegerField()
	message = models.TextField()

	def __str__(self):
		return self.name

class Subscriber(models.Model):
	email=models.EmailField(max_length=300)

	def __str__(self):
		return f"{self.email}"


class Crousal(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='Crousal')
	date = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-date']
