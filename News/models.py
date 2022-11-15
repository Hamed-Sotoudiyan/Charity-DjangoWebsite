from django.db import models

# Create your models here.


class news(models.Model):
    title = models.CharField(max_length=100, blank=False)
    date = models.CharField(blank=False, max_length=100)
    text = models.TextField(blank=False)
    image = models.ImageField(blank=True,upload_to="static/img/news/")

    def __str__ (self):
        return self.title
