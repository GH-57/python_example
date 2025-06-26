"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # chat/urls에 있는 모든 URL 패턴에 일괄적으로
    #  chat/ 라는 prefix 주소를 부여하겠다.
    path('chat/', include('chat.urls')),
    path('blog/', include('blog.urls')),
    path('baemin/', include('baemin.urls')),
    # 어떤 응답을 할까?
    #  - 1) Template을 통해 HTML 응답을 할까?
    #  - 2) 다른 페이지로 이동을 시켜볼 수도 있다
    path('', lambda request: redirect("/baemin/")),
]

# lambda함수는 뒤에 있는 표현식을 평가해서 자동으로 return


# 유저가 업로드한 파일을 서빙하는 View 설정 (View <- 장고 개발서버에서 제공)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
    )

urlpatterns += debug_toolbar_urls()
