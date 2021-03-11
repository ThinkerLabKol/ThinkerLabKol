from django.shortcuts import render, redirect
from django.contrib import messages
from Thinker_Lab.settings import RAZORPAY_KEY_ID, RAZORPAY_SECRET_KEY, EMAIL_HOST_USER
from .models import Coding
from django.core.mail import send_mail

# Razor Pay
import razorpay
from django.views.decorators.csrf import csrf_exempt


def coding(request):
    context = {}

    return render(request, 'coding.html', context)


def coding_registration(request):
    context = {}

    if request.method == "POST":
        name = request.POST.get('name')
        whatsapp_no = request.POST.get('whatsapp_no')
        contact_no = request.POST.get('contact_no')
        email = request.user.email
        class_name = request.POST.get('class_name')
        school = request.POST.get('school')
        category = request.POST.get('category')

        order_amount = 2*100
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'

        client = razorpay.Client(
            auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET_KEY)
        )
        payment = client.order.create(
            {'amount': order_amount, 'currency': order_currency,
                'receipt': order_receipt, 'payment_capture': '1'}
        )

        coding_registration_form = Coding(name=name, whatsapp_no=whatsapp_no, contact_no=contact_no,
                                          email=email, class_name=class_name, school=school, category=category, payment_id=payment['id'])
        coding_registration_form.save()
        messages.success(
            request, f'Congratulations! Your form has been submitted. Please proceed to payment to complete your registration')

        context['name'] = name
        context['mobile_no'] = whatsapp_no
        context['payment'] = payment

        return render(request, 'coding_registration.html', context)

    return render(request, 'coding_registration.html', context)


# Fucntion for successful course payment
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

        user = Coding.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()

        # Sending mail after successful payment for coding registration
        subject = 'Payment Successful'
        message = 'Congratulations! Your payment has been received. Your Order ID: ' + order_id
        reciepient = email
        send_mail(subject, message, EMAIL_HOST_USER, [reciepient])

    return render(request, "success.html")
