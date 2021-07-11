from django.contrib import admin
from .models import Course, Wishlist, Enrollment

admin.site.register(Course)
admin.site.register(Wishlist)
admin.site.register(Enrollment)
