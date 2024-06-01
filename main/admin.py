from django.contrib import admin
from django.urls import path
from django.views.generic import View  # View를 import 추가
from .models import Visitor
from django.http import JsonResponse

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('date', 'daily_count', 'monthly_count', 'total_count')

class VisitorLineChartJSONView(View):
    def get_data(self):
        data = {
            'labels': [str(visitor.date) for visitor in Visitor.objects.all()],
            'datasets': [
                {
                    'label': 'Daily Count',
                    'data': [visitor.daily_count for visitor in Visitor.objects.all()],
                    'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                    'borderColor': 'rgba(255, 99, 132, 1)',
                    'borderWidth': 1
                },
                {
                    'label': 'Monthly Count',
                    'data': [visitor.monthly_count for visitor in Visitor.objects.all()],
                    'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                    'borderColor': 'rgba(54, 162, 235, 1)',
                    'borderWidth': 1
                },
                {
                    'label': 'Total Count',
                    'data': [visitor.total_count for visitor in Visitor.objects.all()],
                    'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                    'borderColor': 'rgba(75, 192, 192, 1)',
                    'borderWidth': 1
                }
            ]
        }
        return data

    def get(self, request, *args, **kwargs):
        data = self.get_data()
        return JsonResponse(data)

# Django admin에 등록
admin.site.register(Visitor, VisitorAdmin)

# admin 페이지에 새로운 URL을 추가하여 VisitorLineChartJSONView를 포함시킴
urlpatterns = [
    path('admin/visitor_chart/', VisitorLineChartJSONView.as_view(), name='visitor_chart'),
]
