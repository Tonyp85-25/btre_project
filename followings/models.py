from django.db import models
from datetime import datetime
# Create your models here.


class Following(models.Model):
    following_date = models.DateTimeField(default=datetime.now)
    user_id = models.IntegerField()
    listing_id = models.IntegerField()
    listing = models.CharField(max_length=200)
