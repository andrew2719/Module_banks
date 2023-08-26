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
    path("get_all_courses/", student.get_all_courses, name="get_all_courses"), #api
    path('get_course/', student.get_course, name='get_course'), #api
    # path('course/<int:course_id>/', views.course, name='course'),
    # path('courses/', views.courses, name='courses'),
    # path('my_courses/', views.my_courses, name='my_courses'),

    # instructor
    path('instructor/', instructor.instructor, name='instructor'),#page
    path('addCourse/', instructor.addCourse, name='addCourse'),#page
]