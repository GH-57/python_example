from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI()

items = {}

class Item(BaseModel):
    name: str # 필수 값 (빈 값 X)
    description: Optional[str] = None 
    # description에 빈 값을 넣을 수도 있다
    price: float


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


@app.post("/items/{item_id}", response_model=Item)
# Item이라는 클래스를 응답받는 모델
def create_item(item_id:int, item:Item):
    if item_id in items:
        raise HTTPException(status_code=400,detail="Item already exisis") # raise 예외는 강제로 에러발생 (미연에 방지)
    items[item_id] = item 

    return item


@app.get("/items", response_model=List[Item])
def read_items():
    return list(items.values())


@app.get("/items/keys", response_model=List[int])
def read_keys(): 
    return list(items.keys())


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id:int):
    if item_id not in items:
        raise HTTPException(status_code=404,detail="Item not found")
    return items[item_id]

