from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app = FastAPI()

notices = ["공지사항1", "공지사항2", "공지사항3"]

templates = Jinja2Templates(directory="templates") #templates

# @app.get("/") # -> 127.0.0.1:8000 get method
# def read_root():
#     return {"이름": "Ho"}


# @app.post("/")
# def post_root():
#     return {"이건": "포스트입니다."}


# @app.get("/good")
# def read_goo():
#     return {"a": 1}


# @app.get("/todo")
# def read_todo():
#     return {"백문이": "불여일타"}


# @app.get("/free")
# def read_free():
#     return {"이무진": "뱁새", "발표": [2025, 5, 27]}


# @app.get("/info")
# def get_info():
#     return {
#         "이름": "max",
#         "주소": {"zipcode": 12345, "주소1": "서울특별시", "주소2": "505"},
#     }


# 실습

@app.get("/")  # -> 127.0.0.1:8000 get method
def read_root():
    return {"Hello": "World"}


@app.get("/about")  # -> 127.0.0.1:8000/about get method
def about():
    return {"message": "about page"}


@app.get("/contact")  # -> 127.0.0.1:8000/contact get method
def contact():
    return {"message": "contact page"}


@app.get("/notice")  # -> 127.0.0.1:8000/notice get method
def notice():
    return {"notice": notices}

##

@app.get("/index", response_class=HTMLResponse)  # HTML 형태 (JSON형태 X)
def index():
    return "<h1> 너무 더워어어어어어어 하겐다즈 줘어어 </h1>"

@app.get("/index2") # ->127.0.0.1:8000/index2 get method
def index2(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})