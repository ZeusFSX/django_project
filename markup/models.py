from django.db import models
from django.conf.global_settings import LANGUAGES


class Article(models.Model):
    TONALITY_CHOICES = [
        ("negative", "Negative sentimental"),
        ("neutral", "Neutral sentimental"),
        ("positive", "Positive sentimental")
    ]
    title = models.CharField(max_length=300, default="")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tonality = models.CharField(max_length=8, choices=TONALITY_CHOICES)
    language = models.CharField(max_length=7, choices=LANGUAGES)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Entity(models.Model):
    TOKENS_CHOICES = [
        ("PER", "Name of person"),
        ("LOC", "Locations"),
        ("ORG", "Organizations"),
        ("DATE", "Date"),
        ("NAT", "Nationality"),
        ("TITLE", "Title or name of position")
    ]
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    offset = models.IntegerField()
    length = models.IntegerField()
    text = models.TextField()
    type_entity = models.CharField(max_length=10, choices=TOKENS_CHOICES)

    def __str__(self):
        return self.text



