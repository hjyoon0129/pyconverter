from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from datetime import datetime

class MainSitemap(Sitemap):
    changefreq = "daily"  # 페이지 업데이트 빈도 (필요에 따라 수정 가능)
    priority = 0.5  # 페이지 우선순위 (필요에 따라 수정 가능)

    def items(self):
        # 사이트맵에 포함할 URL 목록을 반환합니다.
        return ['main:home', 'pyxel:index', 'boarda:index']

    def location(self, item):
        # 각 URL 패턴의 이름에 해당하는 실제 URL을 반환합니다.
        return reverse(item)

    def lastmod(self, item):
        # 페이지의 최근 수정 날짜를 반환합니다. (필요에 따라 수정 가능)
        return datetime.now()
