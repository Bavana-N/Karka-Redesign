from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "duration",
        "created_at",
    )

    list_filter = (
        "category",
        "duration",
    )

    search_fields = (
        "name",
        "category",
    )