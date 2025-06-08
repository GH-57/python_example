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

