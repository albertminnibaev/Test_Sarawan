from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'avatar')

    def get_model_perms(self, request):
        return {
            "add": self.has_add_permission(request),
            "change": self.has_change_permission(request),
            "delete": self.has_delete_permission(request),
            "view": self.has_view_permission(request),
        }

    def has_view_permission(self, request, obj=None):
        allowed = super().has_view_permission(request, obj)
        if object is None:
            return allowed
        return request.user.is_admin or request.user.is_authenticated

    def has_change_permission(self, request, obj=None):
        allowed = super().has_change_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj
        return request.user.is_admin

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        allowed = super().has_delete_permission(request, obj)
        if object is None:
            return allowed
        return request.user.is_admin

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                'is_superuser',
                'is_staff',
                'is_active',
                'is_admin',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True
        return form
