# 사용자 정보를 저장하고 조회하는 API를 만드세요
# 메모리에 저장 (딕셔너리 사용)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

app = FastAPI()

# 사용자 저장소 (메모리)
users = {}  # {user_id: User 객체}
user_counter = 1

# 구현할 엔드포인트:
# 1. POST /users - 사용자 생성, 응답: {"user_id": 1, "message": "사용자가 생성되었습니다"}
# 2. GET /users/{user_id} - 사용자 조회, 응답: User 객체
# 3. GET /users - 모든 사용자 조회, 응답: {"users": [User 객체들]}

# 여기에 코드 작성