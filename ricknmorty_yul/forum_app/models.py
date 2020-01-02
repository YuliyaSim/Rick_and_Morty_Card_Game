from datetime import date

from django.contrib.auth.models import User
from django.db import models

from profile_app.models import Profile

# Create your models here.


class Thread(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Comment(models.Model):
    thread_id = models.ForeignKey(Thread, null=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    date_posted = models.DateField(default=date.today)
    content = models.CharField(max_length=1000)
