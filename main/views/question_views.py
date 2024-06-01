from django.shortcuts import render
from main.models import Question

def home(request):
    main_questions = Question.objects.order_by('-created_at')[:5]

    context = {
        'main_questions': main_questions,
    }
    return render(request, 'main/question_list.html', context)
