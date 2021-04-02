from django.shortcuts import render
from .models import Quiz, Question, Record, Scorecard
from django.core.paginator import Paginator
from django.http import HttpResponse


# Displaying all the available tests
def test_list(request):
    quizes = Quiz.objects.all()
    
    context = {
        'quizes': quizes,
    }

    return render(request, 'quiz_list.html', context)


# Function for any particular test
def test(request, id):
    quiz = Quiz.objects.get(id=id)
    questions = Question.objects.filter(quiz_name=quiz).order_by('id')

    # Pagination
    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        dic = request.POST

        for question in questions:
            # Condition for checking if user has answered the question
            if question.question_title in dic.keys():
                record = Record(quiz_name=quiz, user=request.user, question=question, correct_ans=question.correct_ans , user_ans=dic[question.question_title])
            else:
                record = Record(quiz_name=quiz, user=request.user, question=question, correct_ans=question.correct_ans , user_ans=' ')
            record.save()
        
        return HttpResponse("<h1> You test has been successfully submitted </h1>")

    context = {
        'questions': questions,
        'page_obj': page_obj,
    }

    return render(request, 'quiz.html', context)


def grade_calculation(request):
    pass