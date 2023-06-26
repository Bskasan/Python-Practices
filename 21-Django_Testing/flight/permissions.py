from rest_framework.permissions import IsAdminUser, SAFE_METHODS

class IsAdminOrReadOnly(IsAdminUser):
    
    """
    Allows admin users to make CRUD.
    Allows users (guest or logged in) to list only.
    """

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
