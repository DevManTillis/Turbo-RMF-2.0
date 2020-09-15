from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models

# Create your models here.
class AccountManager(BaseUserManager):
    """Manage & work with our custom user model"""
    def create_user(self, name, email, username, password=None):
        """create a new customer profile"""
        if not email:
            raise ValueError("Valid E-mail address required")

        email = self.normalize_email(email)
        acct = self.model(name=name, email=email, username=username)

        acct.set_password(password)
        acct.save(using=self._db)

        return acct

    def create_superuser(self, name, email, username, password):
        """create and saves new superuser"""
        user = self.create_user(name, email, username, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class AccountProfile(AbstractBaseUser, PermissionsMixin):
    """Represents customers inside the system"""
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)

    date_of_creation = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name", "username"]

    def __str__(self):
        return self.email
