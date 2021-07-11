from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.CourseList.as_view(), name='course-list'),
    path('course/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),

    path('course/<int:pk>/add-to-wishlist/', views.WishListCreate.as_view(), name='add-wishlist'),
    path('course/<int:pk>/enroll/', views.EnrollCourse.as_view(), name='enroll-course'),

    path('wishlist/', views.WishListAll.as_view(), name='wishlist-all'),
    path('wishlist/<int:pk>/', views.WishListDetails.as_view(), name='wishlist-detail'),

]
