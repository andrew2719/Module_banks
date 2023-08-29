from django.shortcuts import render, redirect
# import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout
from Users.models import CustomUser, Student
from Users.models import Instructor
from django.contrib.auth.decorators import login_required,user_passes_test
from App.models import Courses, Mycourses
from django.http import JsonResponse
import random


def instructor(request):
    if request.user.is_authenticated:
        print(request.user.email)
        return render(request, "instructor/instructor_home.html")
    

def addCourse(request):

    if request.method=='POST':
        inst_id = request.user.id
        instructor_id = CustomUser.objects.get(id=inst_id)
        print(instructor_id)
        course_name = request.POST.get('course_name')
        course_image =request.FILES.get('course_image')
        course_description = request.POST.get('course_description')
        course_price = request.POST.get('course_price')
        course_duration = request.POST.get('course_duration')
        course_code = random.randint(100000,999999)
        
        course = Courses(course_name=course_name,
                         course_image=course_image,
                                course_description=course_description,
                                course_price=course_price,
                                course_duration=course_duration,
                                course_code=course_code,
                                instructor_id=instructor_id)
        
        course.save()
        return redirect('instructor')
    print(request.user.id)
    return render(request, "instructor/add_course.html")