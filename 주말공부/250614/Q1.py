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



@app.post("/users")
async def create_user(user: User):
    global user_counter
    users[user_counter] = user
    user_id = user_counter
    user_counter += 1
    return {"user_id": user_id, "message": "사용자가 생성되었습니다"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    return users[user_id]

@app.get("/users")
async def get_all_users():
    return {"users": list(users.values())}