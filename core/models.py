
from django.db import models


class Student(models.Model):
    student_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="University Number",
    )

    fingerprint_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        unique=True,
        verbose_name="Fingerprint Template ID",
    )

    rfid_uid = models.CharField(
        max_length=32,
        blank=True,
        default="",
        verbose_name="RFID Card UID",
    )

    full_name = models.CharField(
        max_length=150,
        verbose_name="Full Name",
    )
    email = models.EmailField(
        blank=True,
        verbose_name="University Email",
    )
    college = models.CharField(
        max_length=100,
        verbose_name="College",
    )
    major = models.CharField(
        max_length=100,
        verbose_name="Major",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
    )

    def __str__(self):
        return f"{self.student_number} - {self.full_name}"

    class Meta:
        ordering = ["student_number"]
        verbose_name = "Student"
        verbose_name_plural = "Students"
