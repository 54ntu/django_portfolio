from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    #custom permission to allow only admin can edit objects
    #other users can only see the details

    def has_permission(self, request, view):
        if view.action in ['list','retrieve']:
            return True
        return request.user.is_superuser