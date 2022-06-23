from rest_framework.permissions import BasePermission


SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            user = request.user
            if hasattr(user, 'is_anonymous') and user.is_anonymous:
                return False
            elif request.method in SAFE_METHODS and user.is_authenticated:
                return True
            elif user.is_admin:
                return True
        return False


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            user = request.user
            if request.method in SAFE_METHODS:
                return True
            elif user.is_admin:
                return True
        return False
