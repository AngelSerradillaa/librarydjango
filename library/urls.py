from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UsuarioList, UsuarioDetail,
    LibroList, LibroCreate, LibroDetail, LibroUpdate, LibroDelete,
    libros_por_autor, UsuarioCreate, UsuarioDelete, AutorCreate, AutorDelete,
    AutorDetail, AutorList,
)

urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetail.as_view(), name='usuario-detail'),
    path('usuarios/nuevo/', UsuarioCreate.as_view(), name='usuario-create'),
    path('usuarios/eliminar/<int:pk>', UsuarioDelete.as_view(), name='usuario-delete'),

    path('autores/nuevo/', AutorCreate.as_view(), name='autor-create'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),
    path('autores/', AutorList.as_view(), name='autor-list'),
    path('autores/eliminar/<int:pk>/', AutorDelete.as_view(), name='autor-delete'),

    path('libros/', LibroList.as_view(), name='libro-list'),
    path('libros/nuevo/', LibroCreate.as_view(), name='libro-create'),
    path('libros/<int:pk>/', LibroDetail.as_view(), name='libro-detail'),
    path('libros/actualizar/<int:pk>/', LibroUpdate.as_view(), name='libro-update'),
    path('libros/eliminar/<int:pk>/', LibroDelete.as_view(), name='libro-delete'),
    path('libros/autor/<int:autor_id>/', libros_por_autor, name='libros-autor'),

    path('token/', obtain_auth_token, name='api-token'),  # Login con token
]