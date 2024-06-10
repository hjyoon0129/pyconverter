from django.db import models

class Question(models.Model):
    # ... (기존 필드들)

    BOARD_CHOICES = [
        ('pyxel', 'Pyxel'),
        ('boarda', 'Board A'),
        ('boardb', 'Board B'),
        # 추가적인 게시판이 있다면 계속 추가
    ]

    category = models.CharField(max_length=20, choices=BOARD_CHOICES)

    def __str__(self):
        return f"{self.subject} - {self.category}"

# visitor/models.py

# main/models.py

from django.db import models
from django.utils import timezone

class Visitor(models.Model):
    date = models.DateField(default=timezone.now)
    daily_count = models.PositiveIntegerField(default=0)
    monthly_count = models.PositiveIntegerField(default=0)
    total_count = models.PositiveIntegerField(default=0)

    @classmethod
    def update_visitor_count(cls, request):
        # 현재 날짜 가져오기
        today = timezone.now().date()

        # 오늘의 방문자 레코드 가져오기
        visitor, created = cls.objects.get_or_create(date=today)

        # 새로 고침할 때만 방문자 수 업데이트
        if not request.session.get('visited_today'):
            # 방문자 수 업데이트
            visitor.daily_count += 1
            visitor.monthly_count += 1
            visitor.total_count += 1

            # 만약 새로운 달이 시작되면 월별 카운트를 초기화
            if today.day == 1:
                cls.objects \
                    .filter(date__year=today.year, date__month=today.month) \
                    .update(monthly_count=0)

            # 데이터베이스에 변경사항 저장
            visitor.save()

            # 방문 여부를 세션에 저장
            request.session['visited_today'] = True

    @classmethod
    def get_daily_count(cls):
        # 오늘의 일별 방문자 수 가져오기
        today = timezone.now().date()
        daily_count = cls.objects.filter(date=today).values_list('daily_count', flat=True).first()

        return daily_count or 0

    @classmethod
    def get_monthly_count(cls):
        # 현재 월의 누적 방문자 수 가져오기
        today = timezone.now().date()
        month_start = today.replace(day=1)
        monthly_count = cls.objects \
            .filter(date__year=today.year, date__month=today.month) \
            .aggregate(monthly_count=models.Sum('daily_count'))['monthly_count']

        return monthly_count or 0

    @classmethod
    def get_total_count(cls):
        # 총 방문자 수 가져오기
        total_count = cls.objects.aggregate(total_count=models.Sum('daily_count'))['total_count']
        return total_count or 0