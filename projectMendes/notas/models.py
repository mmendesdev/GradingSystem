from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Nota(models.Model):
    titulo = models.CharField(max_length=100, verbose_name=_("note title"))
    conteudo = models.TextField(verbose_name=_("content"))
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Owner"))
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, verbose_name=_("category")
    )
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_("created in"))

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
