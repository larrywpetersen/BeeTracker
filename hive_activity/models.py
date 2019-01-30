from django.db import models
from django.urls import reverse


class MiteCountMethod(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')

