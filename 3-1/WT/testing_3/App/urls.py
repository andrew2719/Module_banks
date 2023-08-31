from django.urls import path
from . import views
from App.views_folder import student, instructor
urlpatterns = [
    # login register logout
    path("", views.landing_page, name="landing_page"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_, name="logout"),

    # student
    path("home/", student.home, name="home"), #page
    path("profile/", student.client_profile, name="profile"), #page
    path("courses/", student.courses, name="courses"), #page
    path("my_courses/", student.my_courses, name="my_courses"), #page
    path("get_all_courses/", student.get_all_courses, name="get_all_courses"), #api
    path('get_course/', student.get_course, name='get_course'), #api
    path('courses/<int:course_code>', student.course, name='course_page'), #page
    path('course_page/', student.course_page, name='course_page'), #page

    # instructor
    path('instructor/', instructor.instructor, name='instructor'),#page
    path('addCourse/', instructor.addCourse, name='addCourse'),#page

    path('enroll_course/', student.enroll_course, name='enroll_course'), #api
    path('unenroll_course/', student.unenroll_course, name='unenroll_course'), #api
    path('check_enrolled/<str:courseCode>', student.check_enrolled, name='check_enrolled'), #api
    
]