from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# django view : http 요청을 받아 요청을 처리하는 함수
#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능
# @app.get("/chat/") # FastAPI style
def index(request: HttpRequest) -> HttpResponse:
    # query parameters, form data, files, headers, etc.

    # str (html, text), image data, pdf data, streaming, etc.

    # html_str = "<html><head></head><body><h1>hello django in html</h1></body>"

    # # return HttpResponse("Hello Django")
    # return HttpResponse(html_str)  # deFault content type:  text/html

    # html도 장고 입장에서는 그냥 텍슽츠, 이 외에 다양한 포멧도 문자열이면 가능
    return render(request, "chat/index.html")
