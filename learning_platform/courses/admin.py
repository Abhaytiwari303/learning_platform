from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Superusers see all; instructors see only their own
        if request.user.is_superuser:
            return qs
        return qs.filter(instructor=request.user)

    def has_change_permission(self, request, obj=None):
        # Only allow changing if they are the instructor
        if obj is not None and not request.user.is_superuser:
            return obj.instructor == request.user
        return True

    def has_delete_permission(self, request, obj=None):
        # Only allow deleting if they are the instructor
        if obj is not None and not request.user.is_superuser:
            return obj.instructor == request.user
        return True

    def save_model(self, request, obj, form, change):
        # Automatically assign the instructor
        if not obj.pk:
            obj.instructor = request.user
        obj.save()

admin.site.register(Course, CourseAdmin)
