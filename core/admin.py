
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_number",
        "full_name",
        "college",
        "major",
        "fingerprint_id",
        "rfid_uid",
        "is_active",
    )

    search_fields = (
        "student_number",
        "full_name",
        "email",
        "rfid_uid",
    )

    list_filter = (
        "college",
        "major",
        "is_active",
    )

    ordering = ("student_number",)

    fields = (
        "student_number",
        "full_name",
        "email",
        "college",
        "major",
        "fingerprint_id",
        "rfid_uid",
        "is_active",
    )
