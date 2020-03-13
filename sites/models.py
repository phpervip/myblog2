from django.db import models

# Create your models here.

class Aritcle(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    body = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title
