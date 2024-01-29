# gestorpass/views.py
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        # Lógica para crear un nuevo usuario
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Lógica para actualizar un usuario existente
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Lógica para eliminar un usuario existente
        return super().destroy(request, *args, **kwargs)

