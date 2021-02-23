from django.urls import path
from .views import all_courses, course_details, lesson_details

urlpatterns = [
    path('courses/', all_courses, name='courses'),
    path('courses/<int:id>/', course_details, name='course-details'),
    path('lesson/<int:id>/', lesson_details, name='lesson-details')
]