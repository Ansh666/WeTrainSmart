from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from api.user.models import CustomUser

class TrainerManager(BaseUserManager):
    def create_trainer(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        trainer = self.model(email=email, **extra_fields)
        trainer.set_password(password)
        trainer.save(using=self._db)
        return trainer

class Trainer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=20, unique=True)
    name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male')
    dob = models.DateField(default='2000-01-01')
    contact_no = models.CharField(max_length=20, default=False)
    state = models.CharField(max_length=50, default='New Delhi')
    domain = models.CharField(max_length=100, choices=[
        ('Yoga Trainer', 'Yoga Trainer'),
        ('Fitness Trainer', 'Fitness Trainer'),
        ('Aerobics', 'Aerobics'),
        ('Zumba', 'Zumba'),
        ('Dietitian', 'Dietitian'),
        ('Nutritionist', 'Nutritionist'),
        ('Sujok Trainer', 'Sujok Trainer'),
        ('Special Population', 'Special Population'),
        ('Rehabilitation', 'Rehabilitation'),
        ('Coach', 'Coach'),
        ('Athlete', 'Athlete'),
        ('Resource', 'Resource'),
        ('Academy', 'Academy'),
        ('Gym', 'Gym'),
        ('Other', 'Other'),
    ], default='other')
    session_token = models.CharField(max_length=1, default='0')
    


    # Unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='trainer_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='trainer_user_permissions',
        blank=True,
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = TrainerManager()

    def __str__(self):
        return self.name