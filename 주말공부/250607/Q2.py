'''
문제 2: 쿼리 매개변수 기초
간단한 계산기 API
'''

from fastapi import FastAPI

app = FastAPI()

# /add 경로에 GET 요청으로 쿼리 매개변수 a, b를 받아서
# 두 숫자를 더한 결과를 {"result": 합계} 형태로 반환하세요
# 예: /add?a=5&b=3 → {"result": 8}


@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}