from django.db import models
from .categoria import Categoria
from .editora import Editora
from .autor import Autor

#models.ForeignKey: define o campo como sendo uma chave estrangeira.
#Categoria: o model que será associado a esse campo.
#on_delete=models.PROTECT: impede de apagar uma categoria que possua livros associados.
#related_name="livros": cria um atributo livros na classe Categoria, permitindo acessar todos os livros de uma categoria.
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros")
    editora = models.ForeignKey(Editora, on_delete = models.PROTECT, related_name="editoras")
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="autor")
    def __str__(self):
        return f"{self.titulo} ({isbn})"