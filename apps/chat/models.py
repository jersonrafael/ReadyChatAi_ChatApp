from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class message(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    to = models.CharField(max_length=300)
    text = models.TextField()
    send_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner}"