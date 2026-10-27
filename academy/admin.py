from django.contrib import admin
from .models import Course
from .models import Event

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
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "event_type",
        "event_date",
        "is_published",
    )

    list_filter = (
        "event_type",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = ("event_date",)
