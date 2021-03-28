from django.shortcuts import render
from .models import Quiz, Question
from django.core.paginator import Paginator


def test_list(request):
    quizes = Quiz.objects.all()
    
    context = {
        'quizes': quizes,
    }

    return render(request, 'quiz_list.html', context)

def test(request, id):
    quiz = Quiz.objects.get(id=id)
    questions = Question.objects.filter(quiz_name=quiz).order_by('id')

    # Pagination
    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'questions': questions,
        'page_obj': page_obj,
    }

    return render(request, 'quiz.html', context)