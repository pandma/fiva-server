from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    p1 = models.CharField(max_length=50)
    p2 = models.CharField(max_length=50)
    p3 = models.CharField(max_length=50)
    p4 = models.CharField(max_length=50)
    p5 = models.CharField(max_length=50)
    p6 = models.CharField(max_length=50)
