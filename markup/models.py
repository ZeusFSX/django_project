from django.db import models
from django.conf.global_settings import LANGUAGES


class Article(models.Model):
    TONALITY_CHOICES = [
        ("negative", "Negative sentimental"),
        ("neutral", "Neutral sentimental"),
        ("positive", "Positive sentimental")
    ]
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tonality = models.CharField(max_length=8, choices=TONALITY_CHOICES)
    language = models.CharField(max_length=7, choices=LANGUAGES)

    def __str__(self):
        return self.text[:100]

    class Meta:
        ordering = ['-date']


# class Entity(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)