from django.shortcuts import render, redirect
# import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout
from Users.models import CustomUser, Student, Instructor
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Courses, Mycourses
from django.http import JsonResponse


def login_request(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print("Login Success")
            if user.role == "student":
                return redirect("home")
            else:
                return redirect("instructor")
                
        else:
            print("Login Failed")

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        role = request.POST.get("role")
        print(role)
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(name, email, password)
            
        # add them to the database
        user = CustomUser.objects.create_user(email=email, password=password, name=name, role=role)
        # user.save()
        print(user)
        if role == "student":
            student = Student.objects.create(user=user,education="NA",ranking=0)
            student.save()
        else:
            instructor = Instructor.objects.create(user=user,qualification="NA")
            instructor.save()
                
        if user is not None and (role == "student" or role == "instructor"):
            print("User Created")
            return redirect("login")
        else:
            print("User Not Created")

    
    return render(request, "register.html")
    
def logout_(request):
    logout(request)
    return redirect("login")


# def home(request):
#     # if authenticated then show home page
#     if request.user.is_authenticated:
#         print(request.user.email)
#         return render(request, "student/home.html")
#     # we can use @login_required decorator to check if user is authenticated or not

# def instructor(request):
#     if request.user.is_authenticated:
#         print(request.user.email)
#         return render(request, "instructor/instructor_home.html")

# def client_profile(request):
#     if request.user.is_authenticated:
#         # get the id
#         id = request.user.id
#         print(id)
#         # get the user data
#         user = CustomUser.objects.get(id=id)
#         courses_details = Mycourses.objects.filter(student_id=id)
#         print(courses_details)
#         data = {"user":user, "courses_details":courses_details}
#         return render(request, "student/client_profile.html", data)
    
# def course(request, course_id):
#     if request.user.is_authenticated:
#         print(request.user.email)
#         # data = Courses.objects.get(id=course_id)
#         # data need to be passed to the template
#         return render(request, "student/course.html") # static page
    
# def courses(request): # page for displaying all the courses list
    
#     # if request.method=='GET':
#     #     courses = Courses.objects.all()
#     #     # print(courses)
#     #     data = [{"course_name":course.course_name, "course_code":course.course_code} for course in courses]
#     #     # print(data)
#     #     return JsonResponse({"courses":data})

#     return render(request, "student/courses.html")

# def get_all_courses(request):
#     if request.method == 'GET':
#         courses = Courses.objects.all()
#         # print(courses)
#         data = [{"course_name":course.course_name, "course_code":course.course_code} for course in courses]
#         # print(data)
#         return JsonResponse({"courses":data})

# def get_course(request):
#     if request.method == 'GET':
#         text = request.GET.get('course','')
#         # print(text)
#         data = Courses.objects.get(course_name=text)
#         # print(type(data))
#         # print(data.course_code)
#         return JsonResponse({"course_name":data.course_name, "course_code":data.course_code})
        

# def my_courses(request): # page for displaying courses that are enrolled by the user
#     if request.user.is_authenticated:
#         print(request.user.email)

#         return render(request, "student/my_courses.html")
    
# def search(request):

#     if request.method == 'GET':
#         search_text = request.GET.get('query','')

#         if search_text:
#             courses = Courses.objects.filter(course_name__icontains=search_text)

#             course_data = [{"course_name":course.course_code} for course in courses]

#             return JsonResponse({"courses":course_data})
        
        
#     return JsonResponse({"message: No courses found"})
            