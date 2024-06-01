# main/views.py

from django.shortcuts import render
from ..models import Question, Visitor

def home(request):
    questions = Question.objects.all()

    # Visitor 모델의 update_visitor_count 함수를 호출하여 방문자 수 업데이트
    Visitor.update_visitor_count(request)

    # 일별, 월별 및 총 방문자 수 가져오기
    daily_count = Visitor.get_daily_count()
    monthly_count = Visitor.get_monthly_count()
    total_count = Visitor.get_total_count()

    context = {
        'questions': questions,
        'daily_count': daily_count,
        'monthly_count': monthly_count,
        'total_count': total_count,
    }

    return render(request, 'main/question_list.html', context)
