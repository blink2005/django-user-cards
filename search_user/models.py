from django.db import models

class Information(models.Model):
    fio = models.TextField()
    country = models.TextField()
    address = models.TextField()
    telephone = models.TextField()
    description = models.TextField()