from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # auth users only can see list view
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request cause now the users is authenticated
        # here is GET method
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permissions are only allowed to the author of the post
        # here the user can make UPDATE or DELETE
        return obj.author == request.user