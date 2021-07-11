from rest_framework import serializers
from .models import Course, Wishlist, Enrollment, User


class UserSerializer(serializers.ModelSerializer):
    """
    id, first_name, last_name, username fields from User model
    """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']


class EnrolledSerializer(serializers.ModelSerializer):
    """
    Enrolled users - only username
    """
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Enrollment
        exclude = ('enrolled_course',)


class CourseSerializer(serializers.ModelSerializer):
    """
    ALl the course details - course_name, author_name, created_date, price
    """

    class Meta:
        model = Course
        fields = "__all__"

    def validate_course_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Course name too short!")
        return value


class CourseEnrolledSerializer(serializers.ModelSerializer):
    """
    ALl the course details with enrolled users - course_name, author_name, created_date, price, users_enrolled
    """

    users_enrolled = EnrolledSerializer(many=True, read_only=True, source="filter_enrolled_users")

    class Meta:
        model = Course
        fields = "__all__"

    def validate_course_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Course name too short!")
        return value


class WishListSerializer(serializers.ModelSerializer):
    """
    Wishlist course and users added
    """
    wishlist_user = UserSerializer(read_only=True)
    wishlist_course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Wishlist
        fields = "__all__"
