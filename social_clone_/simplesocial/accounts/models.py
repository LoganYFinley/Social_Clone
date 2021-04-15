from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        # username below comes with 'auth.models.User'
        return f"@{self.username}"