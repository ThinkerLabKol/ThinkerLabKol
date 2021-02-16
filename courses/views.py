from django.shortcuts import render
from .models import *
from django.db.models import Q

def all_courses(request):
    courses = Course.objects.all()
    lessons = Lessons.objects.all()

    # if request.method == "GET":
    #     searched_course = request.GET.get('q')
    #     course_list = Course.objects.filter(Q(course_name__icontains=searched_course))

    context = {
        'courses': courses,
        'lessons': lessons,
        # 'course_list': course_list,
    }

    return render(request, 'courses.html', context)

def course_details(request, id):
    course = Course.objects.get(id=id)

    context = {
        'course': course,
    }

    return render(request, 'course_details.html', context)