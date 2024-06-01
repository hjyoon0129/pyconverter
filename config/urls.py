from django.contrib import admin
from django.urls import include, path
from pyxel.views import base_views as pyxel_base_views
from boarda.views import base_views as boarda_base_views
from boardb.views import base_views as boardb_base_views
from humor.views import base_views as humor_base_views
from main.views import base_views as main_base_views
from qna.views import base_views as qna_base_views
# from visitor.views import base_views as visitor_base_views
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import MainSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'main': MainSitemap,
}

urlpatterns = [
    path('main/', include('main.urls')),
    path('boardb/', include('boardb.urls')),
    path('boarda/', include('boarda.urls')),
    path('pyxel/', include('pyxel.urls')),
    path('common/', include('common.urls')),
    path('humor/', include('humor.urls')),
    path('qna/', include('qna.urls')),
    # path('visitor/', include('visitor.urls')),
    path('admin/', admin.site.urls),

    path('', main_base_views.home, name='home'),  # '/' 에 해당되는 path
    path('', pyxel_base_views.index, name='index'),
    path('', boarda_base_views.index, name='index'),
    path('', boardb_base_views.index, name='index'),
    path('', humor_base_views.index, name='index'),
    path('', qna_base_views.index, name='index'),
    # path('', visitor_base_views.index, name='index'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    # 또는 boarda_base_views.index를 사용할 수 있습니다, 필요에 따라 선택하세요.
]
# 개발 서버에서 미디어 파일 서빙
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

