from django.db import models

# Create your models here.


class contactus (models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=30, blank=False)
    message = models.TextField(blank=False)

    def __str__ (self):
        return self.full_name
