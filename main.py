from fastapi import FastAPI
app = FastAPI()

 


@app.get("/")
async def root():
    return {"message":"welcome to my api"}


@app.get("/post")
def get_post():
    return {"data":"This is your posts"}