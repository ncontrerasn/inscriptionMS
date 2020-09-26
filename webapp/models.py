from django.db import models


class Inscription(models.Model):
    id = models.AutoField(primary_key = True)
    id_curso = models.IntegerField()
    id_usuario = models.IntegerField()
    max_activity = models.IntegerField()

