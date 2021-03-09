from django.shortcuts import render

def coding(request):
    context = {}

    return render(request, 'coding.html', context)
