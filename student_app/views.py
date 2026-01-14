from django.shortcuts import render, redirect
from .models import Student

def home(request):
    return render(request, "base.html")

def student_list(request):
    students = Student.objects.all().order_by("-id")
    return render(request, "students.html", {"students": students})

def student_add(request):
    if request.method == "POST":
        Student.objects.create(
            full_name=request.POST.get("full_name"),
            age=request.POST.get("age"),
            roll_number=request.POST.get("roll_number"),
            enrollment_date=request.POST.get("enrollment_date"),
        )
    return redirect("home")

def student_update(request):
    if request.method == "POST":
        roll_number = request.POST.get("roll_number")

        try:
            student = Student.objects.get(roll_number=roll_number)

            full_name = request.POST.get("full_name")
            age = request.POST.get("age")
            enrollment_date = request.POST.get("enrollment_date")

            if full_name:
                student.full_name = full_name
            if age:
                student.age = age
            if enrollment_date:
                student.enrollment_date = enrollment_date

            student.save()

        except Student.DoesNotExist:
            pass

    return redirect("home")

def student_delete(request):
    if request.method == "POST":
        roll_number = request.POST.get("roll_number")

        try:
            student = Student.objects.get(roll_number=roll_number)
            student.delete()
        except Student.DoesNotExist:
            pass

    return redirect("home")
