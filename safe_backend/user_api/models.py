from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class AppUserManager(BaseUserManager):
	def create_user(self, email, password=None, username=None, birth_date=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		if not username:
			raise ValueError('A username is required.')
		if not birth_date:
			raise ValueError('A birth date is required.')
		email = self.normalize_email(email)
		user = self.model(email=email, username=username, birth_date=birth_date)
		user.set_password(password)
		user.save()
		return user
	def create_superuser(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(email, password)
		user.is_superuser = True
		user.save()
		return user
    
class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    birth_date = models.DateField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'birth_date']
    objects = AppUserManager()
    def __str__(self):
        return self.username