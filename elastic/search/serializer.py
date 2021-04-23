from rest_framework import serializers
from .models import Biblioteca

#Seralizer de los documentos enviados a elastic search
class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = "__all__"
