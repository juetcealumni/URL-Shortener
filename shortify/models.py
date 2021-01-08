from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    id=models.AutoField
    long_url=models.URLField(max_length=500,blank=True)
    short_url=models.URLField(max_length=100,blank=True)
    def __str__(self):
        return str(self.id)