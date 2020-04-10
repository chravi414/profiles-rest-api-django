from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
	"""Manager for User profiles"""

	def create_user(self, email, name, password=None):
		""" Create a new user Profile"""
		if not email:
			raise valueError('Users must have an email address')

		email = self.normalize_email(email)

		user = self.model(email=email, name=name)

		user.set_password(password)

		user.save(using=self._db)

		return user


	def create_superuser(self, email, name, password):
		""" Create and save a new super user """
		user = self.create_user(email, name, password)

		user.is_staff = True
		
		user.is_superuser = True

		user.save(using=self._db)

		return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Database Model for User in the system"""
	email = models.EmailField(max_length=250, unique=True)
	name = models.CharField(max_length=250)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		"""Retrieve Full Name of User"""
		return self.name

	def get_short_name(self):
		"""Retrieve short name of User"""
		return self.name

	def __str__(self):
		"""Return string representation of User"""
		return self.email


