from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def index():
    return {"message":"メインページです。"}



@app.get("/greeting")
async def greeting():
    print("Hello")
    return {"message":"FastAPIだよ"}


# export port 8080
handler = Mangum(app)