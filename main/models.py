from django.db import models

from django.contrib.gis.db import models


class Land(models.Model):
    farmer_name = models.CharField(max_length=255)
    location = models.PointField()
    crops = models.CharField(max_length=255)
    season = models.CharField(max_length=255, choices=[
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('autumn', 'Autumn'),
        ('winter', 'Winter')
    ])

    def __str__(self):
        return self.farmer_name
