from django.contrib import admin
from .models import UserCalendar


@admin.register(UserCalendar)
class UserCalendarAdmin(admin.ModelAdmin):
    list_display = ("pk", "owner", "title", "created_at", "updated_at")
    list_display_links = ("pk", "owner", "title")
    search_fields = ("owner",)
