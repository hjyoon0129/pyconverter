from django.shortcuts import redirect

def social_login_redirect(request, provider):
    # provider에 따라 각 소셜 인증 제공업체의 로그인 URL로 리다이렉트합니다.
    if provider == 'google':
        # Google 로그인 URL로 리다이렉트
        return redirect('google_login_url')
    elif provider == 'kakao':
        # Kakao 로그인 URL로 리다이렉트
        return redirect('kakao_login_url')
    else:
        # 지원되지 않는 소셜 인증 제공업체일 경우 예외 처리
        return HttpResponseBadRequest("Unsupported provider")