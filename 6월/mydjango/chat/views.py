from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from chat.models import PuzzleRoom

# django view : http 요청을 받아 요청을 처리하는 함수 
# => 장고 에서는 클래스로 View를 만들것이다. 
# => 클래스 기반 뷰 (Class Based View, etc)

#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능
# @app.get("/chat/") # FastAPI style

# 채팅 기본 화면을 보여준다.
def index(request: HttpRequest) -> HttpResponse:
    # query parameters, form data, files, headers, etc.

    # str (html, text), image data, pdf data, streaming, etc.

    # html_str = "<html><head></head><body><h1>hello django in html</h1></body>"

    # # return HttpResponse("Hello Django")
    # return HttpResponse(html_str)  # deFault content type:  text/html

    # html도 장고 입장에서는 그냥 텍슽츠, 이 외에 다양한 포멧도 문자열이면 가능
    return render(request, "chat/index.html")


# 매 채팅 메시지를 받아, 응답 메시지를 만들고, 응답한다.
# HTTP Methods: GET, POST, PUT/PATCH, DELETE, OPTIONS
# - HTTP: 웹 페이지, 웹 문서를 위한 프로토콜
# - <form>태그(유저로부터 입력을 받아 지정 서버로 전송) 에서는 GET, POST만 지원
#   - GET: 조회 목적 => 요청해도 데이터는 변하지 않는다. 안정하다 =>ex) 검색엔진
#   - POST: 파괴적인 액션(추가/수정/삭제 등)
#     - 조회목적인데 POST 요청을 하는 서비스가 있다(경우에 따라) 
#       가급적이면 조회에서는 GET 요청을 쓰면, 서비스를 최적화를 여지가 많고
#       이를 도와주는 서비스/프로그램도 많다
# - JS API를 통해서 PUT/PATCH, DELETE 등의 요청을 할 수 있다.
def chat_message_new(request: HttpRequest) -> HttpResponse:
    # Query Parameters
    request.GET # QueryDict 타입 (Dict 으로 보여도 90% 무방)
    request.POST # POST 데이터 (QueryDict)

    question = request.POST.get("question", "")
    if question:
        answer = f"당신의 질문: {question}"
    else:
        answer = "질문이 없으시네요"
    
    return HttpResponse(answer)

# url encoding = "key=value&key=value&key=value&key=value"
# url encoding 문자열이 요청 주소 뒤에 물음표(?) 뒤에 붙으면 
# => 그게 Query Parameters
'''
where=nexearch
sm=top_hty
fbm=0
ie=utf8
query=python
ackey=4rvenuph
'''

# TODO: 왜 puzzle_room_list가 아니라 puzzleroom_list 인가요?
def puzzleroom_list(request):
    # puzzle room 테이블에 있는 모든 레코드를 가져올 준비
    qs = PuzzleRoom.objects.all()
    return render(
        request, 
        template_name="chat/puzzleroom_list.html",
        context={"puzzleroom_list": qs})



# chat/urls.py에서 name 인자를 추출해서
# View 함수 호출 시에 자동으로 인자를 전달해줍니다.

def puzzle_room(request: HttpRequest, name: str) -> HttpResponse:

    # 외부로부터 젅달맏은 값은 절대 신뢰하지 말고
    # 원하는 규칙에 맞는지, 항상 검사해야 한다.

    # 없는 데이터를 요청했는 데, 500 서버 에러로 기록되는 것은 서버 개발자는 억울합니다.
    # 없는 데이터는 404 Page not found 응답을 하는 것이 맞습니다.

    # TODO: image_url/level 설정을 View 단에 하드 코딩이 아니라
    # 유저가 이미지와 레벨을 설정해서 방을 만들면 좋겠다.
    # => 이러한 보통은 데이터베이스에 저장/수정하고 불러서 활용한다.
    #    보통의 애플리케이션들은 대개 데이터베이스 중심의 소프트웨어이다.

    try:
        image_url = {
            "mario": "/static/chat/mario.jpg",
            "toy": "/static/chat/toy-story.jpg",
            "kirby": "/static/chat/kirby.jpg",
            "openai-1": "/static/chat/openai-1.png",
        }[name]
    except KeyError:
        # 위에서 임포트 : from django.http import Http404
        raise Http404(f"not found room : {name}")
    
    level = 3 # or 4, 5

    # toy, mario, flower, game
    return render(
        request,
        # 이 템플릿 내의 코드는 모두 문자열!!
        template_name="chat/puzzle.html",
        # "image_url"이라는 이름으로 image_url 값을 전달
        # 대개 같은 이름으로 지정한다
        context={
            "image_url": image_url,
            "level": level,
            },
        
    )  