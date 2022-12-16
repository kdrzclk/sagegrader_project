from django.db import models
import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    inst_name = models.CharField(unique=True, max_length=50)
    inst_city = models.CharField(max_length=50)
    inst_state_code = models.CharField(max_length=50)
    inst_country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.inst_name} - {self.inst_city} - {self.inst_country} '


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("Email is mandatory")
        # if not username:
        #     raise ValueError("USers must have a username")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField('email address', unique=True)
    # username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    institutions = models.ForeignKey(Institution, models.DO_NOTHING, related_name='institutions', null=True)

    ADMIN = "Admin"
    TEACHER = "Teacher"
    MARKER = "Marker"

    USER_ROLE = [
        (ADMIN, "Admin"),
        (TEACHER, "Teacher"),
        (MARKER, "Marker")
    ]
    user_role = models.CharField(max_length=7, choices=USER_ROLE, default=ADMIN)
    user_create_date = models.DateTimeField(auto_now_add=True)
    user_is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # is_superuser is defined at PermissionsMixin
    # password and last_login defined at AbstractBaseUser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email