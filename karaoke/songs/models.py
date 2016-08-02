from django.db import models

# Write your models here
class Performer(models.Model):
  name = models.CharField(max_length=255)  
  def __str__(self):
      return self.name

class Song(models.Model):
  title = models.CharField(max_length=255)
  artist = models.CharField(max_length=255)
  length = models.IntegerField(default=0)
  performer = models.ForeignKey(Performer, default=1)
  
  def __str__(self):
      return '%s %s' % (self.title, self.artist)


    
  