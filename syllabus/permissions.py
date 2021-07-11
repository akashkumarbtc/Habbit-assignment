from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    """
    If user is not admin allow GET request
    """
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission
