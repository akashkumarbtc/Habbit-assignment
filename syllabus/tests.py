from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from . import models


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.course = models.Course.objects.create(course_name="Python Course", author_name="sam", price=1000)

    def test_create_course(self):
        data = {
            "course_name": "sample",
            "author_name": "akash",
            "price": "1000"
        }
        response = self.client.post(reverse('course-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_course_list(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_single(self):
        response = self.client.get(reverse('course-detail', args=(self.course.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_update(self):
        data = {
            "course_name": "Python",
            "author_name": "akash",
            "price": "1000"
        }
        self.user1 = User.objects.create_user(username="example1", password="Password123", is_staff=True)
        self.client.force_authenticate(user=self.user1)
        response = self.client.put(reverse('course-detail', args=(self.course.id, )), data)
        self.assertEqual(models.Course.objects.get().course_name, "Python")


class WishlistTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.course = models.Course.objects.create(course_name="Python Course", author_name="sam", price=1000)
        self.wishlist = models.Wishlist.objects.create(wishlist_user=self.user, wishlist_course=self.course, confirm=True)

    def test_wishlist_all(self):
        response = self.client.get(reverse('wishlist-all'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wishlist_single(self):
        response = self.client.get(reverse('wishlist-detail', args=(self.wishlist.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Wishlist.objects.get().wishlist_course.course_name, "Python Course")
        self.assertEqual(models.Wishlist.objects.get().wishlist_user.username, "example")


class WishlistCreateTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.course = models.Course.objects.create(course_name="Python Course", author_name="sam", price=1000)

    def test_wishlist_create(self):
        data = {
            "confirm": "True"
        }
        response = self.client.post(reverse('add-wishlist', args=(self.course.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('add-wishlist', args=(self.course.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauthenticate_create(self):
        data = {
            "confirm": "True"
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('add-wishlist', args=(self.course.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



class EnrolledTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.course = models.Course.objects.create(course_name="Python Course", author_name="sam", price=1000)

    def test_enroll_create(self):
        data = {
            "confirm": "True"
        }
        response = self.client.post(reverse('enroll-course', args=(self.course.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('enroll-course', args=(self.course.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)





