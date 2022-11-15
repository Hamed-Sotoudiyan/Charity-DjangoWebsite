from django.db import models

# Create your models here.


class supporters (models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=30,blank=False)
    city = models.CharField(max_length=30, blank=False)
    sms = models.BooleanField(default=True)

    def __str__ (self):
        return self.full_name

class financialsAids(models.Model):
    supporter = models.ForeignKey(supporters,on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=False)

    def __str__ (self):
        return self.price
