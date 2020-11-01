from django.db import models

# Create your models here.
class ContactFormModel(models.Model):
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=2043)
