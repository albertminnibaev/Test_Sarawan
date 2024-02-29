from django.contrib import admin

from .models import Category, Subcategory, Product, Gallery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'image')
    prepopulated_fields = {"slug": ("title",)}

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
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        allowed = super().has_change_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj.author
        return request.user.is_admin

    def has_add_permission(self, request):
        allowed = super().has_add_permission(request)
        if object is None:
            return allowed
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        allowed = super().has_delete_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj.author
        return request.user.is_admin


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'image', 'category')
    prepopulated_fields = {"slug": ("title",)}

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
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        allowed = super().has_change_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj.author
        return request.user.is_admin

    def has_add_permission(self, request):
        allowed = super().has_add_permission(request)
        if object is None:
            return allowed
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        allowed = super().has_delete_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj.author
        return request.user.is_admin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'image', 'price', 'subcategory', 'set_gallery')
    prepopulated_fields = {"slug": ("title",)}

    def set_gallery(self, obj):
        gallery = [i.__str__() for i in obj.gallery_set.all()]
        return gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'product')

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
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        allowed = super().has_change_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj.author
        return request.user.is_admin

    def has_add_permission(self, request):
        allowed = super().has_add_permission(request)
        if object is None:
            return allowed
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        allowed = super().has_delete_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj.author
        return request.user.is_admin
