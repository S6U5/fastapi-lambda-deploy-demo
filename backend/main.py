from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def index():
    return {"message":"メインページです。"}



@app.get("/greeting")
async def greeting():
    print("Hello")
    return {"message":"今日の挨拶"}

@app.get("/goodbye")
async def greeting():
    print("さようなら")
    return {"message":"永遠の別れ"}


# export port 8080
handler = Mangum(app)