from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'
        TRAINER = 'trainer', 'Trainer'
        
    base_role = Role.USER
    
    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
    name = models.CharField(max_length=50, default='Name')
    email = models.EmailField(max_length=50, unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone = models.CharField(max_length=20, blank=False, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    session_token = models.CharField(max_length=1, default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.name} ({self.email})"

