from django.db import models

# Модель MainForm

class Application(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    service = models.CharField(max_length=64)
    comment = models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
