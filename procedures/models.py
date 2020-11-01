from django.db import models

# Create your models here.
class Procedure(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later

    def __str__(self):
        txt = self.code + " - " + self.title
        return str(txt)

    def snippet(self):
        return self.body[:50] + '...'
