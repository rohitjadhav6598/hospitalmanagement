from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Patient(models.Model):
	name = 	models.CharField(max_length=30)
	age = models.IntegerField()
	doa = models.DateField(default=timezone.now)
	address = models.TextField()

	def __str__(self):
		return self.name