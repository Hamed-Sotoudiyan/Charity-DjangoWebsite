from django.db import models

# Create your models here.


class video(models.Model):
    lecturer_name = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    video_url = models.TextField(blank=False)
    image = models.ImageField(blank=True,upload_to="static/img/videos_images/")

    def __str__ (self):
        return self.lecturer_name
