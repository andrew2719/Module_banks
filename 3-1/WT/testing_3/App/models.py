from django.db import models
from Users.models import CustomUser


class Courses(models.Model): # all the courses table
    course_name = models.CharField(max_length=100)
    #course code is a primary key
    course_image = models.ImageField(upload_to='course_images', null=True)
    course_code = models.CharField(max_length=100, primary_key=True)
    course_description = models.CharField(max_length=100, null=True)
    course_duration = models.CharField(max_length=100, null=True)
    no_of_assignments = models.IntegerField(null=True)
    course_price = models.CharField(max_length=100, null=True)
    instructor_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.course_name
    

class Mycourses(models.Model): # student enrolled courses

    # student id and course code is the primary key


    # course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    # student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    # both the course and student id are primary keys
    class Meta:
        unique_together = ('course', 'student_id',)
        
    # progress is the percentage
    no_of_assignmetns_completed = models.IntegerField(null=True)

    def __str__(self):
        return self.course.course_name
    
