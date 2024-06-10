from django import forms
from pdf.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'image', 'recommendation']

        labels = {
            'subject': '제목',
            'content': '내용',
        }
