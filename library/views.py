from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Libro, Autor
from .serializers import UsuarioSerializer, LibroSerializer, AutorSerializer
from .permissions import IsAdminUserDelete  # Importamos el permiso personalizado

# Vistas de Usuarios
class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = []  # Permitir acceso sin autenticación

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = []  # Permitir acceso sin autenticación

# Vista para CREAR un usuario
class UsuarioCreate(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = []  # Permitir acceso sin autenticación

# Vista para ELIMINAR un usuario
class UsuarioDelete(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUserDelete]  # Solo usuarios autenticados pueden eliminar

    """def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtener el usuario a eliminar
        self.perform_destroy(instance)  # Eliminar el usuario

        # Actualizar los IDs de los usuarios
        self.renumerar_ids(Usuario)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def renumerar_ids(self, model):
        # Obtener todos los objetos en orden por ID
        objetos = model.objects.all().order_by('id')
        for nuevo_id, objeto in enumerate(objetos, start=1):
            objeto.id = nuevo_id  # Cambiar el ID al nuevo ID
            objeto.save(update_fields=['id'])  # Guardar el objeto con el nuevo ID"""

# Vista para crear un autor
class AutorCreate(generics.CreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = []  # Permitir acceso sin autenticación

# Vista para obtener los detalles de un autor
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = []  # Permitir acceso sin autenticación

# Vista para listar todos los autores
class AutorList(generics.ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = []  # Permitir acceso sin autenticación

# Vista para eliminar un autor
class AutorDelete(generics.DestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [IsAdminUserDelete]  # Si solo administradores pueden eliminar

# Vistas de Libros
class LibroList(generics.ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = []  # Permitir acceso sin autenticación

class LibroCreate(generics.CreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = []  # Permitir acceso sin autenticación

class LibroDetail(generics.RetrieveAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = []  # Permitir acceso sin autenticación

# Vista para actualizar un libro
class LibroUpdate(generics.UpdateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = []  # Permitir acceso sin autenticación

# Vista para eliminar un libro
class LibroDelete(generics.DestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAdminUserDelete]  # Si solo administradores pueden eliminar

# API View: Libros por usuario
@api_view(['GET'])
@permission_classes([IsAdminUserDelete])
def libros_por_autor(request, autor_id):
    try:
        # Obtener el autor por su ID
        autor = Autor.objects.get(id=autor_id)
    except Autor.DoesNotExist:
        return Response({'error': 'Autor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    # Filtrar los libros por el autor especificado
    libros = Libro.objects.filter(autor=autor)
    serializer = LibroSerializer(libros, many=True)
    return Response(serializer.data)
