from django.db import models

class Editora(models):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=100, null=True)
    def __str__(self):
        return self.nome