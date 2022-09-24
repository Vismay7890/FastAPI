from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"welcome to my api"}

# defining type of parameter
# @app.get("/items/{item_id}")
# async def item(item_id: int):
#     return {"item_id":item_id}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_items(skip: int = 0 , limit: int = 10):
    return fake_items_db[skip : skip + limit]


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str , q:str |None = None , short: bool = False):
#     item = {"item_id",item_id}
#     if q:
#         item.update({"q":q})
#     if not short:
#         item.update(
#             {"description":"This is amazing item which has long description"}
#         )
#     return item

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
