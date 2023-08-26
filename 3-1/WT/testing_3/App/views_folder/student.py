from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from Users.models import CustomUser, Student, Instructor
from django.contrib.auth.decorators import login_required,user_passes_test
from App.models import Courses, Mycourses
from django.http import JsonResponse

def home(request):
    # if authenticated then show home page
    if request.user.is_authenticated:
        print(request.user.email)
        return render(request, "student/home.html")
    
    
def client_profile(request):
    if request.user.is_authenticated:
        # get the id
        id = request.user.id
        print(id)
        # get the user data
        user = CustomUser.objects.get(id=id)
        courses_details = Mycourses.objects.filter(student_id=id)
        print(courses_details)
        data = {"user":user, "courses_details":courses_details}
        return render(request, "student/client_profile.html", data)
    
def course(request, course_id):
    if request.user.is_authenticated:
        print(request.user.email)
        # data = Courses.objects.get(id=course_id)
        # data need to be passed to the template
        return render(request, "student/course.html") # static page
    
def courses(request): # page for displaying all the courses list
    
    # if request.method=='GET':
    #     courses = Courses.objects.all()
    #     # print(courses)
    #     data = [{"course_name":course.course_name, "course_code":course.course_code} for course in courses]
    #     # print(data)
    #     return JsonResponse({"courses":data})

    return render(request, "student/courses.html")

def get_all_courses(request):
    if request.method == 'GET':
        courses = Courses.objects.all()
        # print(courses)
        data = [{"course_name":course.course_name, "course_code":course.course_code} for course in courses]
        # print(data)
        return JsonResponse({"courses":data})

def get_course(request):
    if request.method == 'GET':
        text = request.GET.get('course','')
        # print(text)
        data = Courses.objects.get(course_name=text)
        # print(type(data))
        # print(data.course_code)
        return JsonResponse({"course_name":data.course_name, "course_code":data.course_code})
        

def my_courses(request): # page for displaying courses that are enrolled by the user
    if request.user.is_authenticated:
        print(request.user.email)

        return render(request, "student/my_courses.html")
