# visitor/apps.py

from django.apps import AppConfig

class VisitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visitor'
    app_label = 'visitor'  # 이 부분을 추가합니다.
