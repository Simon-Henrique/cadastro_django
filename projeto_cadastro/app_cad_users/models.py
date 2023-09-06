from django.db import models

# Create your models here.

class user(models.Model):
    id_user = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()