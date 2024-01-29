# Los modelos:
from django.db import models

class Usuario(models.Model):  # Cambiar a Usuario
    nickname = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname

