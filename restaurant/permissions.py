from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated or request.method in SAFE_METHODS)
        