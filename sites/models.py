from django.db import models
from datetime import date

# There are Demosite, Abcsite, Xyzsite models
# and each model has created_date, a_value
# and b_value variables


class Demosite(models.Model):
    created_date = models.DateField(default=date.today)
    a_value = models.FloatField(default=0.00)
    b_value = models.FloatField(default=0.00)


class Abcsite(models.Model):
    created_date = models.DateField(default=date.today)
    a_value = models.FloatField(default=0.00)
    b_value = models.FloatField(default=0.00)


class Xyzsite(models.Model):
    created_date = models.DateField(default=date.today)
    a_value = models.FloatField(default=0.00)
    b_value = models.FloatField(default=0.00)
