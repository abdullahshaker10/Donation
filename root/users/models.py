from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from root.users.enums import UserRoles

from .managers import CustomUserManager

class Role(models.Model):
    name = models.CharField(max_length=255, choices=UserRoles.value_name_choices(),unique=True)
    def __str__(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.ForeignKey("Role", on_delete=models.CASCADE, related_name="users", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email




class Permission(models.Model):
    name = models.CharField(max_length=255, choices=UserRoles.all_permissions(),unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="permissions")

    def __str__(self):
        return self.name
