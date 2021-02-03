from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import UserRegistrationForm
from django.contrib import messages


# ------------------------ User Registration ------------------------
def register_user(request):
    registration_form = UserRegistrationForm()

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            user = registration_form.cleaned_data.get('username')
            messages.success(request, f'Congratulations! Account has been successfuly created for ' + '"' + user + '"')
            return redirect('register-user')
        else:
            messages.warning(request, f'Oops! something went wrong. Please fill data correctly')
    else:
        registration_form = UserRegistrationForm()

    context = {'registration_form': registration_form}

    return render(request, 'register_user.html', context)

def user_login(request):
    context = {}

    return render(request, 'register_user.html', context)