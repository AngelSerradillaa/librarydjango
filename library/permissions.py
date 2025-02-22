# permissions.py
from rest_framework.permissions import BasePermission

class IsAdminUserDelete(BasePermission):
    """
    Permite eliminar usuarios solo si el usuario autenticado tiene es_admin=True.
    """

    def has_permission(self, request, view):
        # Si la petición es DELETE, el usuario debe estar autenticado y ser admin
        if request.method == "DELETE":
            return request.user.is_authenticated and getattr(request.user, "es_admin", False)
        return True  # Permite todos los demás métodos sin autenticación