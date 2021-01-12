from django.db import models

class Clean(models.Model):
    # Уборка
    place = models.CharField(max_length=64)
    type_clean = models.CharField(max_length=64)
    type_rooms = models.CharField(max_length=64)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
