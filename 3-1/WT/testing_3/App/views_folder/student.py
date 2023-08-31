from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from Users.models import CustomUser, Student, Instructor
from django.contrib.auth.decorators import login_required,user_passes_test
from App.models import Courses, Mycourses
from django.http import JsonResponse
import json
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
    
# def course(request, course_id):
#     if request.user.is_authenticated:
#         print(request.user.email)
#         # data = Courses.objects.get(id=course_id)
#         # data need to be passed to the template
#         return render(request, "student/course.html") # static page
    
def courses(request): # page for displaying all the courses list
    return render(request, "student/courses.html")

def get_all_courses(request):
    if request.method == 'GET':
        courses = Courses.objects.all()
        
        # print(courses)
        # data = [{"course_name":course.course_name,
        #           "course_code":course.course_code,
        #           "course_code":course.course_code} for course in courses]

        data = []
        for course in courses:
            data.append({
                "course_name":course.course_name,
                "course_code":course.course_code,
                "course_image":course.course_image.url
            })
            print(course.course_image.url)
        # print(data)
        return JsonResponse({"courses":data})

def get_course(request):
    if request.method == 'GET':
        text = request.GET.get('course','')
        # print(text)
        data = Courses.objects.get(course_name=text)
        # print(type(data))
        # print(data.course_code)
        course_data = {"course_name":data.course_name, 
                       "course_code":data.course_code,
                       "course_image":data.course_image.url}
        return JsonResponse({"course_data":course_data})
        

def my_courses(request): # page for displaying courses that are enrolled by the user
    if request.user.is_authenticated:
        print(request.user.email)

        return render(request, "student/my_courses.html")

def course(request, course_code):
    if request.user.is_authenticated:
        print(course_code)
        data = Courses.objects.get(course_code=course_code)
        print(data)
        # get the instructor data
        instructor_data = Instructor.objects.get(user=data.instructor_id.id)
        print(instructor_data)
        # print(type(data))
        # # print(data.objects.all())
        # cc = data.pk
        # print(cc)
        # print(data.instructor_id.name)
        course_details = {"course_name":data.course_name,
                          "course_image":data.course_image.url,
                           "course_code":data.course_code, 
                           "course_description":data.course_description, 
                           "course_duration":data.course_duration,
                           "no_of_assignments":data.no_of_assignments,
                            "course_price":data.course_price,
                            "instructor_id":data.instructor_id.name,
                            "qualifications":instructor_data.qualification}
        print(course_details)
        # need to fetch instructor details....
        #  print the id that the course will have by the django
        return render(request,'student/course.html', {'course_details':course_details})
    

def enroll_course(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        course_code = data.get('course_code')

        print(course_code)
        
        course = Courses.objects.get(course_code=course_code)
        print(course)
        student_id = request.user.id
        student = CustomUser.objects.get(id=student_id)
        print(student)
        # # enroll the student
        enroll = Mycourses.objects.create(course=course, student_id=student)
        enroll.save()
        if enroll:
            return JsonResponse({"success":True})
        else:
            return JsonResponse({"success":False})

      
def check_enrolled(request,courseCode):
    course = Mycourses.objects.filter(course=courseCode, student_id=request.user.id)
    print(course)

    if course:
        return JsonResponse({"success":True})
    else:
        return JsonResponse({"success":False})


def unenroll_course(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        course_code = data.get('course_code')
        print(course_code)
        course = Courses.objects.get(course_code=course_code)
        print(course)
        student_id = request.user.id
        student = CustomUser.objects.get(id=student_id)
        print(student)
        # # enroll the student
        unenroll = Mycourses.objects.filter(course=course, student_id=student).delete()
       
        if unenroll:
            return JsonResponse({"success":True})
        else:
            return JsonResponse({"success":False})
        

def course_page(request):
    return render(request, "student/course_page.html")