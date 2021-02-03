from django.shortcuts import render

def register_user(request):
    context = {}

    return render(request, 'register_user.html', context)

