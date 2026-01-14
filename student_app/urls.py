from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.student_list, name="student_list"),

    path("add/", views.student_add, name="student_add"),
    path("update/", views.student_update, name="student_update"),
    path("delete/", views.student_delete, name="student_delete"),
]
