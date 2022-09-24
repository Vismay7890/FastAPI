from fastapi import FastAPI , Query
app = FastAPI()
# @app.get("/items/")
# async def read_items(q:str = Query(default = ... , min_length = 3)):
#     result  = {"items":[{"item_id":"foo"},{"item_id":"bar"}]}
#     if q:
#         result.update({"q":q})
#     return result


# Required with None
@app.get("/items/")
async def read_items(q:str |None = Query(default = ... , min_length = 3)):
    result  = {"items":[{"item_id":"foo"},{"item_id":"bar"}]}
    if q:
        result.update({"q":q})
    return result