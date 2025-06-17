from django.urls import path
from . import views

urlpatterns = [
    # 아래에서 곧 구현합니다.
    # 이 코드를 저장하시면 개발서버에서 index 함수를 찾지못해 오류가 발생할 것이지만,
    # 아래 chat/views.py 저장 후에는 해당 오류가 사라질 것입니다.
    path("", views.index),
]