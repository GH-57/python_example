'''
문제 1: POST 요청 기초
이름과 나이를 받아서 간단한 메시지를 반환하는 API
'''

from fastapi import FastAPI

app = FastAPI()

# /greet 경로에 POST 요청으로 {"name": "홍길동", "age": 25} 형태의 데이터를 받아서
# {"message": "안녕하세요, 홍길동님! 나이는 25세이군요."} 를 반환하세요



@app.post("/greet")
def greet_user(name: str, age: int):
    return {"message": f"안녕하세요, {name}님! 나이는 {age}세이군요."}

