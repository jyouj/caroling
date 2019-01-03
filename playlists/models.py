from django.db import models
import uuid
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey

# Create your models here.
class Title(SortableMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['the_order']

    def __str__(self):
        return self.name

class Song(SortableMixin):
    title = SortableForeignKey(Title, on_delete=models.CASCADE)
    turn = models.CharField(max_length=30)
    song_name = models.CharField(max_length=50)
    artist = models.CharField(max_length=30)
    youtube = models.CharField(max_length=150, blank=True, null=True)
    link = models.CharField(max_length=150, blank=True, null=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['the_order']

    def __str__(self):
        return self.song_name
