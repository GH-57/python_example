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


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author: str
    created_at: datetime


@app.post("/posts")
async def create_post(post: Post):
    post_data = {
        "id": len(posts) + 1,
        "title": post.title,
        "content": post.content,
        "author": post.author,
        "created_at": datetime.now()
    }
    posts.append(post_data)
    return {"message": "게시글이 작성되었습니다", "post_id": post_data["id"]}

@app.get("/posts")
async def get_all_posts():
    return {"posts": posts}

@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다")