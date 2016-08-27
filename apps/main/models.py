from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User

# Create your models here.
class Friendships(models.Model):
    user = models.ForeignKey('loginreg.User', models.DO_NOTHING, related_name="usersfriend")
    friend = models.ForeignKey('loginreg.User', models.DO_NOTHING, related_name ="friendsfriend")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)