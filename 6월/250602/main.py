from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI()

items = {}


class Item(BaseModel):
    name: str  # 필수 값 (빈 값 X)
    description: Optional[str] = None
    # description에 빈 값을 넣을 수도 있다
    price: float
    active: bool = True


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


@app.post("/items/{item_id}", response_model=Item)
# Item이라는 클래스를 응답받는 모델
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(
            status_code=400, detail="Item already exisis"
        )  # raise 예외는 강제로 에러발생 (미연에 방지)
    items[item_id] = item

    return item


@app.get("/items", response_model=List[Item])
def read_items():
    return list(items.values())


@app.get("/items-keys", response_model=List[int])
def read_keys():
    return list(items.keys())


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    stored_item: Item = items[item_id]
    print(
        f"stored_item name={stored_item.name} price={stored_item.price} description={stored_item.description}"
    )
    update_data = item.model_dump(exclude_unset=True)  # 기본값 제외
    # update_data = item.dict # dict의 밑줄 의미"왠만하면 쓰지마" 의미
    print(update_data)

    updated_item = stored_item.model_copy(update=update_data)

    print(
        f"update_item name={updated_item.name} price={updated_item.price} description= {updated_item.description}"
    )

    items[item_id] = updated_item
    return updated_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    items.pop(item_id)  # hard delete ->데이터 완전히 제거


@app.put("/items/{item_id}/active")
def update_active(item_id: int, status: bool = True):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    stored_item: Item = items[item_id]

    if stored_item.active == status:
        raise HTTPException(status_code=400, detail="이미 활성화 되었거나 비활성화 된 아이템입니다.")
    
    stored_item.active = status
    return stored_item
