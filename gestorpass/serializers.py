# gestorpass/serializers.py
from rest_framework import serializers
from .models import Usuario  # Actualizar el import

class UsuarioSerializer(serializers.ModelSerializer):  # Cambiar a UsuarioSerializer
    class Meta:
        model = Usuario  # Actualizar el modelo
        fields = '__all__'  # Puedes ajustar los campos según sea necesario


