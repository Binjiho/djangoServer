from rest_framework.permissions import BasePermission


class AllowEveryOnePermission(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_student)


class IsParents(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_parents)


class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_admin)


class IsAcademyAdministrator(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_academy_admin)


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_teacher)


class IsAssistant(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_assistant)


class IsSoftBridge(BasePermission):
    def has_permission(self, request, view):
        if DEBUG:
            return bool(int(request.user.id) == 40)
        else:
            return bool(int(request.user.id) == 40)
