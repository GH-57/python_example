'''
문제 1: 간단한 할일 관리 API
다음 요구사항을 만족하는 FastAPI 애플리케이션을 작성하세요.
요구사항

/todos (GET): 모든 할일 목록을 반환
/todos/{todo_id} (GET): 특정 ID의 할일을 반환
/todos (POST): 새로운 할일을 추가
할일 데이터 구조: {"id": int, "title": str, "completed": bool}

조건

데이터는 메모리에 저장 (리스트 사용)
Pydantic 모델을 사용해서 요청/응답 데이터 검증
존재하지 않는 ID 조회시 404 에러 반환

예시 응답
json{
  "id": 1,
  "title": "FastAPI 공부하기",
  "completed": false
}
'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic 모델
class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

# 메모리 저장소
todos = []
next_id = 1

@app.get("/todos", response_model=List[Todo])
async def get_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate):
    global next_id
    new_todo = {
        "id": next_id,
        "title": todo.title,
        "completed": todo.completed
    }
    todos.append(new_todo)
    next_id += 1
    return new_todo

