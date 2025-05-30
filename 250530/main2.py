from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

items = []


@app.get("/item")
def item_list():
    return {"item": items}


@app.post("/item/create") # post: 데이터를 추가
def create_item(item: dict):
    items.append(item)
    return {"item": item}
