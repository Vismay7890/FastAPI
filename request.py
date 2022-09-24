from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name :str
    Description:str |None = None
    price:float
    tax:float|None = None
    


app = FastAPI()
# @app.post("/items/")
# async def create_item(item:Item):
#     item_dict = item.dict()
#     if item.tax:
#         total_price = item.price + item.tax
#         item_dict.update({"Price_with_tax":total_price})
#     return item_dict


# request body + path parameter
# @app.post("/items/{item_id}")
# async def create_item(item_id:int , item:Item):
#     return {"item":item_id,**item.dict()}

# request body + path + query parameter
@app.post("/items/{item_id}")
async def create_item(item_id:int , item:Item , q:str|None = None):
    result = {"item":item_id,**item.dict()}
    if q:
        result.update({"q":"kuch or"})
    return result

