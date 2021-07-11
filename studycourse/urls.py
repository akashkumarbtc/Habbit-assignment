from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('syllabus/', include('syllabus.urls')),
    path('account/', include('user_app.urls')),
]
