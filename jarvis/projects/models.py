from django.db import models
from clients.models import Client

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client)

    def __str__(self):
        return str(self.name)
