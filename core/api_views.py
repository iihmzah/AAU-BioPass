import json
import secrets

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from .models import Student


@require_GET
def api_status(request):
    return JsonResponse({
        "success": True,
        "system": "AAU-BioPass",
        "message": "API is running",
    })


def device_is_authenticated(request):
    provided_key = request.headers.get("X-API-Key", "")
    configured_key = settings.ESP32_API_KEY

    return bool(configured_key) and secrets.compare_digest(
        provided_key,
        configured_key,
    )


@csrf_exempt
@require_POST
def api_fingerprint_lookup(request):
    if not device_is_authenticated(request):
        return JsonResponse({
            "success": False,
            "message": "Unauthorized",
        }, status=401)

    try:
        data = json.loads(request.body)
        fingerprint_id = data.get("fingerprint_id")

        if fingerprint_id is None or isinstance(fingerprint_id, bool):
            return JsonResponse({
                "success": False,
                "message": "fingerprint_id is required",
            }, status=400)

        fingerprint_id = int(fingerprint_id)

        if fingerprint_id <= 0:
            raise ValueError

    except (json.JSONDecodeError, TypeError, ValueError):
        return JsonResponse({
            "success": False,
            "message": "Invalid fingerprint_id",
        }, status=400)

    student = Student.objects.filter(
        fingerprint_id=fingerprint_id,
        is_active=True,
    ).first()

    if student is None:
        return JsonResponse({
            "success": False,
            "message": "No active student found",
        }, status=404)

    return JsonResponse({
        "success": True,
        "student": {
            "student_number": student.student_number,
            "full_name": student.full_name,
            "college": student.college,
            "major": student.major,
        },
    })