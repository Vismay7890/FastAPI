from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str ,q: Union[str ,None]= None , short:bool = False):
    item = {"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"This is a long description"})    
    return item