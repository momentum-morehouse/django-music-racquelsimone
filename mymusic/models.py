from django.db import models

# Create your models here.

class Album(models.Model):
  artist_name = models.CharField(max_length=255, null=True, blank=True)
  album_title = models.CharField(max_length=255, null=True, blank=True)
  date_released = models.DateField(null = True, blank=True)

  def _str_(self):
    return f"{self.album_title}"