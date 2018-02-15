from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, full_name='', password=None, active=True):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=UserManager.normalize_email(email),
            full_name=full_name,
        )
        if password:
            user.set_password(password)
        user.is_active = active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name='', password=None):
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=250, blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, app_label):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.full_name


class Company(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'
