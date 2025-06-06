'''
문제 2: 경로 매개변수 사용하기
다음 요구사항에 맞는 FastAPI 코드를 작성하세요:

/user/{name} 경로에 GET 요청을 받는 API
URL에서 name 값을 받아서 {"message": "Hello, {name}!"} 형태로 응답
예: /user/김철수 요청 시 {"message": "Hello, 김철수!"} 응답

힌트: 함수 매개변수에 경로 변수를 받으면 됩니다.
'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{name}")
def get_user(name: str):
    return {"message": f"Hello, {name}!"}
