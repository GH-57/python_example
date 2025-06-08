'''
문제 2: 간단한 계산기 API
다음 요구사항을 만족하는 FastAPI 애플리케이션을 작성하세요.
요구사항

/calculate/add?a=10&b=5 (GET): 두 수를 더한 결과 반환
/calculate/subtract?a=10&b=5 (GET): 두 수를 뺀 결과 반환
/calculate/multiply (POST): 요청 본문의 두 수를 곱한 결과 반환
/calculate/divide (POST): 요청 본문의 두 수를 나눈 결과 반환

조건

GET 요청은 쿼리 파라미터 사용
POST 요청은 JSON 본문 사용: {"a": float, "b": float}
0으로 나누기 시도시 400 에러와 적절한 메시지 반환
결과는 {"result": float} 형태로 반환

예시 요청/응답
POST 요청:
json// 요청
{
  "a": 10.5,
  "b": 2.0
}

// 응답
{
  "result": 21.0
}
'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# POST 요청용 모델
class CalculationRequest(BaseModel):
    a: float
    b: float

class CalculationResponse(BaseModel):
    result: float

# GET 요청 - 덧셈
@app.get("/calculate/add", response_model=CalculationResponse)
async def add(a: float, b: float):
    return CalculationResponse(result=a + b)

# GET 요청 - 뺄셈
@app.get("/calculate/subtract", response_model=CalculationResponse)
async def subtract(a: float, b: float):
    return CalculationResponse(result=a - b)

# POST 요청 - 곱셈
@app.post("/calculate/multiply", response_model=CalculationResponse)
async def multiply(request: CalculationRequest):
    result = request.a * request.b
    return CalculationResponse(result=result)

# POST 요청 - 나눗셈
@app.post("/calculate/divide", response_model=CalculationResponse)
async def divide(request: CalculationRequest):
    if request.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    result = request.a / request.b
    return CalculationResponse(result=result)