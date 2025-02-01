from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pikmin/question_detail.html', context)

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    search_option = request.GET.get('search_option', 'all')  # 검색 옵션 추가

    question_list = Question.objects.order_by('-create_date')

    if kw:
        # 검색 옵션에 따라 필터링
        if search_option == 'title':
            question_list = question_list.filter(subject__icontains=kw)
        elif search_option == 'content':
            question_list = question_list.filter(content__icontains=kw)
        elif search_option == 'comment':
            question_list = question_list.filter(answer__content__icontains=kw)
        elif search_option == 'nickname':
            question_list = question_list.filter(author__username__icontains=kw)
        else:  # 'all' or unknown option
            question_list = question_list.filter(
                Q(subject__icontains=kw) |
                Q(content__icontains=kw) |
                Q(answer__content__icontains=kw) |
                Q(author__username__icontains=kw) |
                Q(answer__author__username__icontains=kw)
            ).distinct()

    # 정렬 적용
    question_list = apply_sorting(question_list, request.GET.get('sort_by'))

    paginator = Paginator(question_list, 25)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'search_option': search_option}
    return render(request, 'pikmin/question_list.html', context)

def apply_sorting(question_list, sort_by):
    if sort_by == 'recent':
        return question_list.order_by('-create_date')
    elif sort_by == 'recommend':
        # 여기에 추천순 정렬 코드 추가
        return question_list  # 예시로 그대로 반환
    elif sort_by == 'popular':
        # 여기에 인기순 정렬 코드 추가
        return question_list  # 예시로 그대로 반환
    else:
        return question_list