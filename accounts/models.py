from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
	filename = "{0}.jpg".format(instance.username)
	return '{0}/{1}'.format(instance.username,filename)

# Create your models here.
class User(AbstractUser):

	image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
	bio = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Users"