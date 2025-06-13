# 게시글 작성/조회 API + 데이터 검증
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from typing import List
from datetime import datetime

class Post(BaseModel):
    title: str
    content: str
    author: str
    
    @validator('title')
    def title_must_not_be_empty(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('제목은 필수입니다')
        return v
    
    @validator('content')
    def content_length_check(cls, v):
        if len(v) < 10:
            raise ValueError('내용은 10자 이상이어야 합니다')
        return v

app = FastAPI()

posts = []  # 게시글 저장소

# 구현할 엔드포인트:
# 1. POST /posts - 게시글 작성
# 2. GET /posts - 모든 게시글 조회
# 3. GET /posts/{post_id} - 특정 게시글 조회 (없으면 404 에러)

# 여기에 코드 작성