from django.db import models


class Maximeter_up_to_50(models.Model):
    owner = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=100)
    cups = models.CharField(max_length=100)
    nif = models.CharField(max_length=100)
    quarter_hour_curve = models.CharField(max_length=9999)
    hired_power = models.CharField(max_length=100)
    anual_consumption = models.CharField(max_length=100, blank=True)
    optimal_anual_consumption = models.CharField(max_length=100, blank=True)
    annual_savings = models.CharField(max_length=100, blank=True)
    recomended_power = models.CharField(max_length=100, blank=True)
