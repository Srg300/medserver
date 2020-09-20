from rest_framework import permissions



class IsOwnerOrReadOnly(permissions.BasePermission):
    # получаем запрос
    def has_object_permission(self, request, view, obj):
        # если метод этого запроса безопасный, т.е. входит в SAFE_METHODS
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            # если входит, то возвращаем True
            return True
        # если не безопасный, то проверяет пользователя объекта
        # если пользователь является владельцем объекта то вернет True
        return obj.user == request.user


class IsOwnerandOnlyOwner(permissions.BasePermission):
    # получаем запрос
    def has_object_permission(self, request, view, obj):
        print(request.user)
        # если метод этого запроса безопасный, т.е. входит в SAFE_METHODS
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            # если входит, то возвращаем True
            if obj.user == request.user:
                return True


class IsStaffUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

class IsSuperUser(permissions.BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class IsOwnerOrAdmin(permissions.BasePermission):
    # получаем запрос
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_superuser

class IsPatient(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.owner.user.id == request.user.id) or request.user.is_staff


class IsDoctor(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return bool(obj.doctor.user_id == request.user.id)


class ForDoctorOrSuperUser(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser


class ForRecepi(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.owner.doctor.user.id == request.user.id) or request.user.is_superuser or bool(obj.owner.user.id == request.user.id)