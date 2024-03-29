from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect



class StudentAndAdminLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an admin"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect("students:student-list")
        return super().dispatch(request, *args, **kwargs)


class FacultyAndAdminLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an admin"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect("faculty:faculty-list")
        return super().dispatch(request, *args, **kwargs)


class FacultyAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is a faculty"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_faculty:
            return redirect("classrooms:classroom-list")
        return super().dispatch(request, *args, **kwargs)