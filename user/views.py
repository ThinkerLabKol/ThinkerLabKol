from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserRegistrationForm

from django.core.mail import send_mail
from Thinker_Lab.settings import EMAIL_HOST_USER


def home(request):
    context = {}

    return render(request, 'index.html', context)

# ------------------------ User Registration ------------------------
def register_user(request):
    registration_form = UserRegistrationForm()

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            # Sending mail to user after successful registration
            subject = 'Welcome to Thinker Lab'
            message = 'Contratulations! You have successfully registerd into Thinker Lab. We wish you all the best for your future.'
            reciepient = str(registration_form['email'].value())
            send_mail(subject, message, EMAIL_HOST_USER, [reciepient])

            user = registration_form.cleaned_data.get('username')
            messages.success(request, f'Congratulations! Account has been successfuly created for ' + '"' + user + '"')
            return redirect('login-user')
        else:
            messages.warning(request, f'Oops! something went wrong. Please fill data correctly')
    else:
        registration_form = UserRegistrationForm()

    context = {'registration_form': registration_form}

    return render(request, 'register_user.html', context)


# ------------------------ User Login ------------------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.warning(request, f'Please Fill correct login credentials!')

    context = {}

    return render(request, 'register_user.html', context)


# ------------------------ User Logout ------------------------
def user_logout(request):
    logout(request)
    return redirect('Home')


