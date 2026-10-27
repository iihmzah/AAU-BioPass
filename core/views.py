
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from django.db import models


def home(request):
    return render(request, "core/home.html")



def student_list(request):
    query = request.GET.get("q", "").strip()

    students = Student.objects.all()

    if query:
        students = students.filter(
            models.Q(student_number__icontains=query)
            | models.Q(full_name__icontains=query)
        )

    return render(
        request,
        "core/student_list.html",
        {
            "students": students,
            "query": query,
        },
    )



def student_create(request):
    if request.method == "POST":
        student_number = request.POST.get("student_number", "").strip()
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        college = request.POST.get("college", "").strip()
        major = request.POST.get("major", "").strip()

        if not all([student_number, full_name, college, major]):
            messages.error(request, "Please fill in all required fields.")

        elif Student.objects.filter(student_number=student_number).exists():
            messages.error(request, "This university number already exists.")

        else:
            Student.objects.create(
                student_number=student_number,
                full_name=full_name,
                email=email,
                college=college,
                major=major,
            )
            messages.success(request, "Student added successfully.")
            return redirect("student_list")

    return render(request, "core/student_create.html")

def student_edit(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        student_number = request.POST.get("student_number", "").strip()
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        college = request.POST.get("college", "").strip()
        major = request.POST.get("major", "").strip()

        if not all([student_number, full_name, college, major]):
            messages.error(request, "Please fill in all required fields.")

        elif Student.objects.filter(
            student_number=student_number
        ).exclude(id=student.id).exists():
            messages.error(request, "This university number already exists.")

        else:
            student.student_number = student_number
            student.full_name = full_name
            student.email = email
            student.college = college
            student.major = major
            student.save()

            messages.success(request, "Student updated successfully.")
            return redirect("student_list")

    return render(
        request,
        "core/student_edit.html",
        {"student": student},
    )

def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect("student_list")

    return render(
        request,
        "core/student_delete.html",
        {"student": student},
    )
