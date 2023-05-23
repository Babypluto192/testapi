from django.db import models


# Create your models here.
class DamirsinbaChasti(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    url = models.CharField(max_length=250)
    preview = models.CharField(max_length=250)

