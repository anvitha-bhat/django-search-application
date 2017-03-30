from __future__ import unicode_literals

from django.db import models

class detail(models.Model):
    customer = models.CharField(max_length = 200)
    HP = models.FloatField(default = 0)
    job_number = models.CharField(max_length = 200)
    volume = models.FloatField(default = 0)
    pressure = models.FloatField(default = 0)
    image = models.ImageField(upload_to='images')
    reference = models.ForeignKey('self', on_delete=models.CASCADE)
