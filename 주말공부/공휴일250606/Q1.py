'''
문제 1: 간단한 GET API 만들기
다음 요구사항에 맞는 FastAPI 코드를 작성하세요:

/hello 경로에 GET 요청을 받는 API
응답으로 {"message": "Hello, World!"} JSON 반환
FastAPI 앱 인스턴스 생성 포함

힌트: @app.get() 데코레이터를 사용하세요.
'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello World!"}