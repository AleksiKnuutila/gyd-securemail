from __future__ import unicode_literals

from django.db import models

class PublicKey(models.Model):
    public_key = models.CharField(max_length=500)
    public_key = models.CharField(max_length=100)
