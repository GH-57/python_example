'''
문제 3: 경로 매개변수 + 조건문
짝수/홀수 판별 API
'''

from fastapi import FastAPI

app = FastAPI()

# /check/{number} 경로에 GET 요청으로 숫자를 받아서
# 짝수면 {"number": 4, "type": "짝수"}
# 홀수면 {"number": 5, "type": "홀수"} 를 반환하세요



@app.get("/check/{number}")
def check_number(number: int):
    if number % 2 == 0:
        return {"number": number, "type": "짝수"}
    else:
        return {"number": number, "type": "홀수"}