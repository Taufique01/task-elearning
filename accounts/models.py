from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
USER_ROLE_CHOICES = (

        ('educator', "Educator"),
        ('learner', "Learner"),
    )
class ElearningUser(AbstractUser):

    role = models.CharField(choices=USER_ROLE_CHOICES, max_length=15,null=False)
