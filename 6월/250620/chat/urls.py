from django.urls import path
from . import views

urlpatterns = [
    # 아래에서 곧 구현합니다.
    # 이 코드를 저장하시면 개발서버에서 index 함수를 찾지못해 오류가 발생할 것이지만,
    # 아래 chat/views.py 저장 후에는 해당 오류가 사라질 것입니다.
    path("", views.index),
    # chat/urls에 있는 모든 URL 패턴에 일괄적으로
    #  chat/ 라는 prefix 주소를 부여하겠다.

    path("messages/new/", views.chat_message_new),

    # /chat/puzzle/mario/
    # /chat/puzzle/toy/
    # /chat/puzzle/running/
    # 가급적 이 패턴은 타이트하게 지정하기를 권장
    # => 엉뚱하게 예상치 못한 URL 패턴까지 잡아버리는 상황을 막을 수 있다.

    path("puzzle/", views.puzzleroom_list),
    # puzzle/ 주소 에 문자열 패턴이 있고, 뒤에 / 가 있으면
    path("puzzle/<int:id>/", views.puzzleroom_play),  # ADDED

    path("puzzle/new/", views.puzzleroom_new),

    path("puzzle/<int:id>/edit/", views.puzzleroom_edit),  

]
