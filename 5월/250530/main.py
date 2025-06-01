from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

blogs = ["블로그1번", "블로그2번", "블로그3번", "블로그4번"]


@app.get("/")
def index():
    return {"인사말": "여 반갑고~"}


@app.get("/blog")
def blog_list():
    return {"목록": blogs}


# @app.get("/blog/{post_id}")  # blog/1 blog/2 이런 형식으로 =>동적이다
# def blog_detail(post_id: int):
#     return {"계시물 번호": post_id}
# 라우트 충돌

@app.get("/blog/{post_tag}")
def tag_list(post_tag: str):

    b = []
    for blog in blogs:
        if post_tag in blog:
            b.append(blog)

    return {"블로그 (태그)목록": b}


@app.get("/blog/{post_tag}/{post_author}")  # blog
def tag_author_list(post_tag: str, post_author: str):
    return {"태그": post_tag, "저자": post_author}


@app.get("/hello/{name}")
def hello_name(name: str):
    return {"안녕하세요": name}


@app.get("/calculate/{operation}/{a}/{b}")
def operation(operation: str, a: int, b: int):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return {"error": "Division by zero"}
        result = a / b
    else:
        return {"error": "Invalid operation"}
    
    return {"result": result}