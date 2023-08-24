from django.shortcuts import render, redirect
# import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout
from Users.models import CustomUser, Student
from Users.models import Instructor
from django.contrib.auth.decorators import login_required,user_passes_test
from App.models import Courses, Mycourses
from django.http import JsonResponse

def instructor(request):
    if request.user.is_authenticated:
        print(request.user.email)
        return render(request, "instructor/instructor_home.html")