from django.db import models
import uuid

# Create your models here.
class Title(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    turn = models.CharField(max_length=30)
    song_name = models.CharField(max_length=50)
    artist = models.CharField(max_length=30)
    youtube = models.CharField(max_length=150, blank=True, null=True)
    link = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.song_name
    
