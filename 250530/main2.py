from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

items = []


class Item(BaseModel):
    name: str
    price: float = 0  # 규격을 정하기 위해서


@app.get("/item")
def item_list():
    return {"item": items}


@app.post("/item/create")  # post: 데이터를 추가
def create_item(item: Item):
    items.append(item)
    print(item.name, item.price)
    return {"item": item}


@app.put("/item/{item_id}")
def item_update(item_id: int, item: Item):
    items[item_id - 1] = item
    return {"item": item}


users = []  # 임시 DB라고 보면 된다.


class User(BaseModel):
    name: str
    email: str
    age: int


@app.get("/users")
def people_list():
    return {"유저리스트": users}


@app.post("/users") # post이기에 /create는 필요하지 않다
def people_create(user: User):
    users.append(user)
    return {"등록된 유저": user}


@app.put("/users/{User_id}")
def User_inform(User_id: int, user: User):
    users[User_id - 1] = user
    return {"people": user}


@app.delete("/users/{User_id}")
def delete_User(User_id:int):
    del users[User_id - 1]     # 지운다 users[3]
    # hard delete -> 완전히 데이터를 지워버리는 것