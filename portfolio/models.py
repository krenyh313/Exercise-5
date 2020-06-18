from django.db import models

class Message(models.Model):
    name    = models.CharField(max_length=60)
    email   = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
