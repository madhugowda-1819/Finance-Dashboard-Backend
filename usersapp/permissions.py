from rest_framework.permissions import BasePermission, SAFE_METHODS


class RecordPermission(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user.is_authenticated:
            return False

        # Admin → full access
        if user.role == "admin":
            return True

        # Analyst → view records only
        if user.role == "analyst":
            return request.method in SAFE_METHODS

        # Viewer → cannot access records
        if user.role == "viewer":
            return False

        return False


class DashboardPermission(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user.is_authenticated:
            return False

        # All roles can view dashboard
        if user.role in ["viewer", "analyst", "admin"]:
            return request.method in SAFE_METHODS

        return False


class UserPermission(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user.is_authenticated:
            return False

        # Only admin can manage users
        if user.role == "admin":
            return True

        return False