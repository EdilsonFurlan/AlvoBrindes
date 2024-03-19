from django.db import models

class Cliente(models.Model):
    nome=models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=15)
    endereco=models.CharField(max_length=50)

    def __str__(self):
        return self.nome

