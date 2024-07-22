from rest_framework import serializers

from .models import Categoria, Nota


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome"]


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ["id", "titulo", "conteudo", "usuario", "categoria"]
        model = Nota
        fields = ["id", "titulo", "conteudo", "usuario", "categoria"]
