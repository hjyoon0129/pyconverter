from django.urls import path

from .views import base_views, question_views, answer_views

app_name = 'editpdf'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
]