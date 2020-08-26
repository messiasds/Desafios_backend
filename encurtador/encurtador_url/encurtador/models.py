from django.db import models


class URL(models.Model):

    original_url = models.CharField(max_length=100)
    new_url = models.CharField(max_length=10)
    validade = models.DateField(auto_now_add=True)

