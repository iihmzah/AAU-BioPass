
from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.student_create, name="student_create"),
    path(
        "students/<int:student_id>/edit/",
        views.student_edit,
        name="student_edit",
    ),
path(
    "students/<int:student_id>/delete/",
    views.student_delete,
    name="student_delete",
),
path("api/status/", api_views.api_status, name="api_status"),
path(
    "api/fingerprint-lookup/",
    api_views.api_fingerprint_lookup,
    name="api_fingerprint_lookup",
),
]
