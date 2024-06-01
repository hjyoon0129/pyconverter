from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 사용자 추가 필드
    # 예시: 닉네임, 프로필 사진 등
    nickname = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # 사용자의 소셜 인증 ID 저장을 위한 필드
    # 예시: 소셜 로그인에 사용되는 사용자 ID
    social_auth_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
