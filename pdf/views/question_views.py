# from django.shortcuts import render
# from pdf.models import Question
#
# def home(request):
#     pdf_questions = Question.objects.order_by('-created_at')[:5]
#
#     context = {
#         'pdf_questions': pdf_questions,
#     }
#     return render(request, 'pdf/question_list.html', context)
