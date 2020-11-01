from django.db import models


class About(models.Model):
    STATUS = (
       ('Welcome', 'Welcome at Home page'),
       ('About_Us', 'About us page'),
       ('Read_More', 'Read more portions'),
    )

    # […]
    header = models.CharField(
       max_length=32,
       choices=STATUS,
       default='Welcome',
    )
    name = models.CharField(max_length=100)
    sequence = models.IntegerField(default=1)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header + " - " + self.get_header_display()
