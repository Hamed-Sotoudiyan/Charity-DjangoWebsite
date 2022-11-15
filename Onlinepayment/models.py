from django.db import models

# Create your models here.


class payment (models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=30,blank=False)
    amount = models.CharField(max_length=30, blank=False)

    def __str__ (self):
        return self.full_name
