from django.db import models
from django.contrib.auth.models import User

class ZettelCard(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    front_image = models.ImageField(upload_to='zettel_cards/front/')
    back_image = models.ImageField(upload_to='zettel_cards/back/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100)
    cards = models.ManyToManyField(ZettelCard, related_name='tags')

class Topic(models.Model):
    name = models.CharField(max_length=100)
    cards = models.ManyToManyField(ZettelCard, related_name='topics')

class Verse(models.Model):
    book = models.CharField(max_length=50)
    chapter = models.IntegerField()
    verse = models.IntegerField()
    text = models.TextField()

    class Meta:
        unique_together = ('book', 'chapter', 'verse')

class Reference(models.Model):
    card = models.ForeignKey(ZettelCard, on_delete=models.CASCADE, related_name='references')
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)

class MediaResource(models.Model):
    card = models.ForeignKey(ZettelCard, on_delete=models.CASCADE, related_name='media')
    title = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='media_resources/')
    TYPE_CHOICES = [('video', 'Video'), ('book', 'Book'), ('audio', 'Audio')]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

class CustomField(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='custom_fields')
    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=20, choices=[('text', 'Text'), ('number', 'Number'), ('date', 'Date')])

class CustomFieldValue(models.Model):
    field = models.ForeignKey(CustomField, on_delete=models.CASCADE, related_name='values')
    card = models.ForeignKey(ZettelCard, on_delete=models.CASCADE, related_name='custom_values')
    value_text = models.TextField(blank=True, null=True)
    value_number = models.FloatField(blank=True, null=True)