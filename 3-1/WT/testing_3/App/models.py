from django.db import models
from Users.models import CustomUser


class Courses(models.Model): # all the courses table
    course_name = models.CharField(max_length=100)
    #course code is a primary key
    course_code = models.CharField(max_length=100, primary_key=True)
    course_description = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=100)
    no_of_assignments = models.IntegerField(null=True)
    course_price = models.CharField(max_length=100)
    instructor_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.course_name
    

class Mycourses(models.Model): # student enrolled courses
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    # progress is the percentage
    no_of_assignmetns_completed = models.IntegerField(null=True)

    def __str__(self):
        return self.course.course_name
    
