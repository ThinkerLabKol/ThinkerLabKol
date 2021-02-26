from django.shortcuts import render, redirect
from .models import *
# from django.db.models import Q
from django.core.paginator import Paginator
from Thinker_Lab import settings
from django.contrib import messages

# Razor Pay
import razorpay
from django.views.decorators.csrf import csrf_exempt



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


def course_registration(request, id):
    user = request.user
    course_name = Course.objects.get(id=id)
    course_price = course_name.price

    context = {
        'user': user,
        'course_name': course_name,
        'course_price': course_price,
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_no = request.POST.get('num')
        college = request.POST.get('college')
        department = request.POST.get('dept')
        year_of_passing = request.POST.get('yop')

        # Razor Pay 
        order_amount = course_price*100
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
        payment = client.order.create({'amount': order_amount, 'currency': order_currency, 'receipt': order_receipt, 'payment_capture': '1'})

        registration = CourseRegistration(name=name, price=course_price, mobile_no=mobile_no, email=user.email, college=college, department=department, year_of_passing=year_of_passing, payment_id=payment['id'], course_name=course_name)
        registration.save()
        messages.success(request, f'Congratulations! Your form has been submitted. Please complete the payment procedure for complete the registration')

        context['name'] = name
        context['mobile_no'] = mobile_no
        context['payment'] = payment

        return render(request, 'course_registration.html', context)

    return render(request, 'course_registration.html', context)

@csrf_exempt
def success(request):
    if request.method == "POST":
        dic = request.POST
        order_id = ''

        for key, value in dic.items():
            if key == 'razorpay_order_id':
                order_id = value
                break
        
        user = CourseRegistration.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()

    return render(request, "success.html")