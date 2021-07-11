from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    """
    Course is used to store details about the course.
    course_name = name of course
    author_name = author of that course
    created_date = auto field that fills time the course was created
    price = price of that course

    filter_enrolled_users is method to extract all the users enrolled to that particular course
    """
    course_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.course_name

    def filter_enrolled_users(self):
        return Enrollment.objects.filter(enrolled_course=self)


class Wishlist(models.Model):
    """
    Wishlist is used to store details about the user who added an course to wishlist
    wishlist_user = authenticated user who added a course to wishlist
    wishlist_course = actual course added to wishlist
    confirm = true to add to database

    """
    wishlist_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='wishlist_user')
    wishlist_course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, related_name='wishlist_course')
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return str(self.wishlist_course)


class Enrollment(models.Model):
    """
        Enrollment is used to store details about the user who enrolled to a  course.
        user = authenticated user who enrolled to a course
        enrolled_course = actual course enrolled
        confirm = true to add to database

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='enrolled_user')
    enrolled_course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, related_name='enrolled_course')
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return str(self.enrolled_course)

