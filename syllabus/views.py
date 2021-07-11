from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .serializers import CourseSerializer, WishListSerializer, CourseEnrolledSerializer, EnrolledSerializer
from .models import Course, Wishlist, Enrollment
from .permissions import AdminOrReadOnly


class CourseList(generics.ListCreateAPIView):
    """
    CourseList is used to get all the courses available.
    [Request support: GET, POST
    URI             : course/
    serializer      : CourseSerializer]
    Both authenticated and non-authenticated users can invoke GET method.
    GET request has throttling enabled:
    i. Anon throttling is set to 500 Get requests per day
    ii. User Throttling is set to 1000 get requests per day.

    Only users with admin privileges can add new course.
    POST request is only enabled for admin users.
    """
    permission_classes = [AdminOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    CourseDetail is used to get individual course
    [Request support: GET, PUT, DELETE
    URI             : course/<int:pk>/
    serializer      : CourseEnrolledSerializer]

    Provides details about a particular course.
    Each course will list enrolled users details

    """

    permission_classes = [AdminOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseEnrolledSerializer


class WishListAll(generics.ListAPIView):
    """
        WishListAll is used to list all the courses added to wishlist by logged in users
        [Request support: GET
        URI             : wishlist/
        serializer      : WishListSerializer]

        Admin users can get list of all the courses added to wishlist by all users.
        Normal looged in users will get list of all courses added to wishlist only by them.

        """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Wishlist.objects.all()
        else:
            queryset = Wishlist.objects.filter(wishlist_user=self.request.user)
        return queryset

    serializer_class = WishListSerializer


class WishListDetails(generics.RetrieveDestroyAPIView):
    """
        WishListDetails is used to get individual course
        [Request support: GET, DELETE
        URI             : wishlist/<int:pk>/
        serializer      : WishListSerializer]

        Admin users can delete any courses added to wishlist by any users.
        Normal looged in users can delete courses added to wishlist only by them.

        """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Wishlist.objects.all()
        else:
            queryset = Wishlist.objects.filter(wishlist_user=self.request.user)
        return queryset

    serializer_class = WishListSerializer


class WishListCreate(generics.CreateAPIView):
    """
        WishListCreate is used to add a course to wishlist
        [Request support: POST
        URI             : course/<int:pk>/add-to-wishlist/
        serializer      : WishListSerializer]

        Normal looged in users can add courses to wishlist.
        POST method body shall contain { "confirm": True } to confirm addition to wishlist.

        If the course is already added to wishlist Error will be raised with message
        "Already added this course to your wishlist"

        If the confirm is set to False, then course will not be added to wishlist

    """
    permission_classes = [IsAuthenticated]

    serializer_class = WishListSerializer

    def get_queryset(self):
        return Wishlist.objects.all()

    def perform_create(self, serializer):
        if self.request.data['confirm'] in [True, 'true', 'True']:
            pk = self.kwargs.get('pk')
            selected_course = Course.objects.get(pk=pk)

            logged_user = self.request.user
            added_queryset = Wishlist.objects.filter(wishlist_user=logged_user, wishlist_course=selected_course)

            if added_queryset.exists():
                raise ValidationError("Already added this course to your wishlist")

            serializer.save(wishlist_course=selected_course, wishlist_user=logged_user)
        else:
            raise ValidationError("Please set confirm to true to add to wishlist")


class EnrollCourse(generics.CreateAPIView):
    """
            EnrollCourse is used to add a course to wishlist
            [Request support: POST
            URI             : course/<int:pk>/enroll/
            serializer      : EnrolledSerializer]

            Normal looged in users can enroll to a course.
            POST method body shall contain { "confirm": True } to confirm course enrollment.

            If the course is enrolled Error will be raised with message
            "Already enrolled to  this course"

            If the confirm is set to False, then user will not be enrolled to a course

        """
    permission_classes = [IsAuthenticated]

    serializer_class = EnrolledSerializer

    def get_queryset(self):
        return Enrollment.objects.all()

    def perform_create(self, serializer):
        if self.request.data['confirm'] in [True, 'true', 'True']:
            pk = self.kwargs.get('pk')
            selected_course = Course.objects.get(pk=pk)

            logged_user = self.request.user
            added_queryset = Enrollment.objects.filter(user=logged_user, enrolled_course=selected_course)

            if added_queryset.exists():
                raise ValidationError("Already enrolled to  this course")

            serializer.save(enrolled_course=selected_course, user=logged_user)
        else:
            raise ValidationError("Please set confirm to true to enroll to this course")

