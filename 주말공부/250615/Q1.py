# API 키 기반 간단한 인증 시스템
from fastapi import FastAPI, HTTPException, Depends, Header
from typing import Optional

app = FastAPI()

# 유효한 API 키들
VALID_API_KEYS = {
    "user1": "key123",
    "user2": "key456"
}

# 보호된 데이터
secret_data = {
    "user1": {"balance": 1000, "level": "gold"},
    "user2": {"balance": 500, "level": "silver"}
}

# 인증 함수 (의존성)
def verify_api_key(x_api_key: Optional[str] = Header(None)):
    # 여기에 API 키 검증 로직 작성
    pass

# 구현할 엔드포인트:
# 1. GET /public - 인증 없이 접근 가능, 응답: {"message": "누구나 볼 수 있습니다"}
# 2. GET /private - 인증 필요, 응답: 사용자별 데이터
# 3. 헤더에 X-API-Key 없거나 잘못되면 401 에러

# 여기에 코드 작성