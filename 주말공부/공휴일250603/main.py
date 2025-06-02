from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# FastAPI 앱 인스턴스 생성
app = FastAPI(title="학생 정보 관리 시스템", description="메모리 기반 학생 CRUD API")

# Pydantic 모델 정의
class StudentCreate(BaseModel):
    """학생 생성용 모델 (ID 제외)"""
    name: str
    age: int
    major: str
    grade: Optional[str] = None

class StudentResponse(BaseModel):
    """학생 응답용 모델 (ID 포함)"""
    id: int
    name: str
    age: int
    major: str
    grade: Optional[str] = None

# 데이터 저장소 (전역 변수)
students: List[dict] = []
next_id: int = 1

# 초기 테스트 데이터 로드
def load_initial_data():
    global next_id
    initial_students = [
        {"name": "김철수", "age": 20, "major": "컴퓨터공학과", "grade": "2학년"},
        {"name": "이영희", "age": 21, "major": "경영학과", "grade": None},
        {"name": "박민수", "age": 19, "major": "전자공학과", "grade": "1학년"}
    ]
    
    for student_data in initial_students:
        student = {
            "id": next_id,
            **student_data
        }
        students.append(student)
        next_id += 1

# 앱 시작 시 초기 데이터 로드
@app.on_event("startup")
async def startup_event():
    load_initial_data()

# 1. 루트 엔드포인트
@app.get("/")
async def root():
    """API 소개 및 현재 등록된 학생 수 표시"""
    return {
        "message": "학생 정보 관리 시스템 API",
        "total_students": len(students),
        "available_endpoints": ["/students", "/students/{id}"]
    }

# 2. 전체 학생 조회
@app.get("/students", response_model=List[StudentResponse])
async def get_all_students():
    """등록된 모든 학생 정보를 조회"""
    return students

# 3. 특정 학생 조회
@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int):
    """ID로 특정 학생의 상세 정보 조회"""
    for student in students:
        if student["id"] == student_id:
            return student
    
    raise HTTPException(status_code=404, detail="학생을 찾을 수 없습니다")

# 4. 새 학생 등록
@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreate):
    """새로운 학생 정보를 등록"""
    global next_id
    
    new_student = {
        "id": next_id,
        "name": student.name,
        "age": student.age,
        "major": student.major,
        "grade": student.grade
    }
    
    students.append(new_student)
    next_id += 1
    
    return new_student

# 5. 학생 정보 수정
@app.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(student_id: int, student: StudentCreate):
    """기존 학생의 정보를 전체 수정"""
    for i, existing_student in enumerate(students):
        if existing_student["id"] == student_id:
            updated_student = {
                "id": student_id,
                "name": student.name,
                "age": student.age,
                "major": student.major,
                "grade": student.grade
            }
            students[i] = updated_student
            return updated_student
    
    raise HTTPException(status_code=404, detail="학생을 찾을 수 없습니다")

# 6. 학생 정보 삭제
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """특정 학생 정보를 삭제"""
    for i, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(i)
            return {
                "message": f"학생 '{deleted_student['name']}'이(가) 성공적으로 삭제되었습니다",
                "deleted_student": deleted_student
            }
    
    raise HTTPException(status_code=404, detail="학생을 찾을 수 없습니다")
