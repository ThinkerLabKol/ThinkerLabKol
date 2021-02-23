from django.shortcuts import render
from .models import *
# from django.db.models import Q
from django.core.paginator import Paginator

def all_courses(request):
    courses = Course.objects.all()
    lessons = Lessons.objects.all()
    course_categoies = CourseCategory.objects.all()
    memberships = Membership.objects.all()

    # Pagination
    paginator = Paginator(courses, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # if request.method == "GET":
    #     searched_course = request.GET.get('q')
    #     course_list = Course.objects.filter(Q(course_name__icontains=searched_course))

    context = {
        'courses': courses,
        'lessons': lessons,
        'page_obj': page_obj,
        'course_categoies': course_categoies,
        'memberships': memberships,
        # 'course_list': course_list,
    }

    return render(request, 'courses.html', context)

def course_details(request, id):
    course = Course.objects.get(id=id)
    lessons = Lessons.objects.filter(course_name=course)

    context = {
        'course': course,
        'lessons': lessons,
    }

    return render(request, 'course_details.html', context)

def lesson_details(request, id):
    lesson = Lessons.objects.get(id=id)

    context = {
        'lesson': lesson,
    }

    return render(request, 'lesson_details.html', context)