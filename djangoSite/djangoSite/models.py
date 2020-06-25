from django.db import models
from django.contrib.auth.models import User

class Invitee(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone = models.CharField(max_length=100)
    verified = models.DateTimeField(auto_now=False, auto_now_add=False)    

class Invitation(models.Model):
    appwan = models.UUIDField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    georegion = models.UUIDField()
    endpoint = models.UUIDField()