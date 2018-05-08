from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class users(models.Model):
    user=models.OneToOneField(User)
    portfolio=models.URLField(blank=True)
    image=models.ImageField(upload_to="profile_pics",blank=True)
