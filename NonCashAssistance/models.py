from django.db import models

# Create your models here.


class NonCashAssistances (models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=100, blank=False)
    message = models.TextField(blank=False)
    action = models.BooleanField(default=False)

    def __str__ (self):
        return self.full_name
