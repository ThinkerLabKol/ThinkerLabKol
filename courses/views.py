from django.shortcuts import render, redirect
from .models import *
# from django.db.models import Q
from django.core.paginator import Paginator
from Thinker_Lab.settings import RAZORPAY_KEY_ID, RAZORPAY_SECRET_KEY, EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Razor Pay
import razorpay
from django.views.decorators.csrf import csrf_exempt


# Displaying all courses on Dashboard
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


# Displaying Details of any particular course
@login_required(login_url='login-user')
def course_details(request, id):
    course = Course.objects.get(id=id)
    user = request.user
    # Checking if user has registerd to current course and also paid for the course
    validation = CourseRegistration.objects.filter(course_name=course).filter(email=user.email).filter(paid=True)

    context = {
        'course': course,
    }

    # If user has not registered to current course then returning only 1 lesson
    if not validation:
        context['not registered'] = 'not registered'
        lesson = Lessons.objects.filter(course_name=course).first()
        context['lesson'] = lesson
    else:
        context['registered'] = 'registered'

    lessons = Lessons.objects.filter(course_name=course)

    context['lessons'] = lessons

    return render(request, 'course_details.html', context)


# Displaying details of any particular lesson
def lesson_details(request, id):
    lesson = Lessons.objects.get(id=id)

    context = {
        'lesson': lesson,
    }

    return render(request, 'lesson_details.html', context)


# Logic for Course Registration
@login_required(login_url='login-user')
def course_registration(request, id):
    user = request.user
    course_name = Course.objects.get(id=id)
    course_price = course_name.price
    free = Membership.objects.filter(membership_type='Free').first()

    context = {
        'user': user,
        'course_name': course_name,
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_no = request.POST.get('num')
        college = request.POST.get('college')
        department = request.POST.get('dept')
        year_of_passing = request.POST.get('yop')

        # If course is free then directly saving the registration form, no payment is needed
        if course_name.course_type == free:
            registration = CourseRegistration(name=name, mobile_no=mobile_no, email=user.email, college=college,
                                              department=department, year_of_passing=year_of_passing, paid=True, course_name=course_name)
            registration.save()
            messages.success(
                request, f'Congratulations! You have successfully registered for the course')

            return redirect('Home')
            # If course is paid then proceeding payment method before saving registration form
        else:
            # Razor Pay
            order_amount = course_price*100
            order_currency = 'INR'
            order_receipt = 'order_rcptid_11'

            client = razorpay.Client(
                auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET_KEY))
            payment = client.order.create(
                {'amount': order_amount, 'currency': order_currency, 'receipt': order_receipt, 'payment_capture': '1'})

            registration = CourseRegistration(name=name, mobile_no=mobile_no, email=user.email, college=college,
                                              department=department, year_of_passing=year_of_passing, payment_id=payment['id'], course_name=course_name)
            registration.save()
            messages.success(
                request, f'Congratulations! Your form has been submitted. Please complete the payment procedure for complete the registration')

            context['name'] = name
            context['mobile_no'] = mobile_no
            context['payment'] = payment

            return render(request, 'course_registration.html', context)

    return render(request, 'course_registration.html', context)


# Function for successful course payment
@csrf_exempt
def success(request):
    if request.method == "POST":
        email = request.user.email
        dic = request.POST
        order_id = ''

        for key, value in dic.items():
            if key == 'razorpay_order_id':
                order_id = value
                break

        user = CourseRegistration.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()

        # Sending mail after successful payment for course registration
        subject = 'Payment Successful'
        message = 'Congratulations! Your payment has been received. Your Order ID: ' + order_id
        reciepient = email
        send_mail(subject, message, EMAIL_HOST_USER, [reciepient])

    return render(request, "success.html")
