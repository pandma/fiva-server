from email import message
from django.db import models


class Constact_User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    state = models.CharField(max_length=100, default='pocesing')
