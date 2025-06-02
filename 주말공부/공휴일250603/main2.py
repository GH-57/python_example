from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from typing import Optional
import os

app = FastAPI()

# 디렉토리 존재 확인 및 생성
os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

# 템플릿 설정
templates = Jinja2Templates(directory="templates")

# 정적 파일 서빙 (CSS용)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 메모리에 할일 데이터 저장 (실제 프로젝트에서는 데이터베이스 사용)
todos = []
next_id = 1

# 기본 테스트용 데이터
if not todos:
    todos.append({
        "id": 1,
        "title": "샘플 할일",
        "description": "이것은 테스트용 할일입니다",
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "priority": "보통"
    })
    next_id = 2

@app.get("/")
async def root():
    """루트 경로 - 간단한 테스트용"""
    return {"message": "Todo App이 실행 중입니다!", "status": "running"}

@app.get("/todos", response_class=HTMLResponse)
async def read_todos(request: Request):
    """메인 페이지 - 할일 목록과 추가 폼"""
    try:
        # 통계 데이터 계산
        total_count = len(todos)
        completed_count = sum(1 for todo in todos if todo["completed"])
        pending_count = total_count - completed_count
        
        return templates.TemplateResponse("index.html", {
            "request": request,
            "todos": todos,
            "total_todos": total_count,
            "completed_todos": completed_count,
            "pending_todos": pending_count
        })
    except Exception as e:
        # 템플릿이 없는 경우 JSON으로 응답
        return {
            "todos": todos,
            "total_todos": len(todos),
            "error": "템플릿 파일을 찾을 수 없습니다. templates/index.html 파일을 생성해주세요."
        }

@app.post("/add")
async def add_todo(
    request: Request,
    title: str = Form(...),
    description: str = Form(""),
    priority: str = Form(...)
):
    """새 할일 추가"""
    global next_id
    
    # 입력값 정제
    title = title.strip()
    description = description.strip()
    
    # 간단한 유효성 검사
    if not title:
        return RedirectResponse(url="/todos?error=제목을+입력해주세요", status_code=303)
    
    if len(title) > 100:
        return RedirectResponse(url="/todos?error=제목은+100자+이하로+입력해주세요", status_code=303)
    
    if len(description) > 500:
        return RedirectResponse(url="/todos?error=설명은+500자+이하로+입력해주세요", status_code=303)
    
    # 새 할일 생성
    new_todo = {
        "id": next_id,
        "title": title,
        "description": description,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "priority": priority
    }
    
    todos.append(new_todo)
    next_id += 1
    
    # POST 후 리다이렉트 (PRG 패턴)
    return RedirectResponse(url="/todos", status_code=303)

@app.post("/toggle/{todo_id}")
async def toggle_todo(todo_id: int):
    """할일 완료/미완료 상태 토글"""
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = not todo["completed"]
            break
    
    return RedirectResponse(url="/todos", status_code=303)

@app.post("/delete/{todo_id}")
async def delete_todo(todo_id: int):
    """할일 삭제"""
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    
    return RedirectResponse(url="/todos", status_code=303)

@app.get("/stats", response_class=HTMLResponse)
async def read_stats(request: Request):
    """통계 페이지"""
    try:
        # 우선순위별 통계
        priority_stats = {"높음": 0, "보통": 0, "낮음": 0}
        completed_by_priority = {"높음": 0, "보통": 0, "낮음": 0}
        
        for todo in todos:
            priority_stats[todo["priority"]] += 1
            if todo["completed"]:
                completed_by_priority[todo["priority"]] += 1
        
        # 전체 통계
        total_count = len(todos)
        completed_count = sum(1 for todo in todos if todo["completed"])
        pending_count = total_count - completed_count
        
        completion_rate = (completed_count / total_count * 100) if total_count > 0 else 0
        
        return templates.TemplateResponse("stats.html", {
            "request": request,
            "total_todos": total_count,
            "completed_todos": completed_count,
            "pending_todos": pending_count,
            "completion_rate": round(completion_rate, 1),
            "priority_stats": priority_stats,
            "completed_by_priority": completed_by_priority
        })
    except Exception as e:
        return {
            "total_todos": len(todos),
            "completed_todos": sum(1 for todo in todos if todo["completed"]),
            "pending_todos": len(todos) - sum(1 for todo in todos if todo["completed"]),
            "error": "템플릿 파일을 찾을 수 없습니다. templates/stats.html 파일을 생성해주세요."
        }

# 헬스 체크 엔드포인트
@app.get("/health")
async def health_check():
    """서버 상태 확인"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_todos": len(todos)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)