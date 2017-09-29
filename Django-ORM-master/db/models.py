import sys
try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()


class Dado(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
