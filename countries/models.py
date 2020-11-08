from django.db import models

# Create your models here.

class Country(models.Model):
    title = models.CharField(max_length=30)
    currency = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

