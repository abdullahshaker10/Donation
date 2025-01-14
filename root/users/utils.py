from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def has_permission(permission_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(view, request, *args, **kwargs):
            user = request.user
            if user.role and not user.role.permissions.filter(name=permission_name).exists():            
                return Response(
                    {"detail": f"You do not have permission: {permission_name}"},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            return view_func(view, request, *args, **kwargs)
        
        return _wrapped_view
    return decorator