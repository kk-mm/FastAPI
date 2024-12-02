from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello Kyaw Kyaw, You are Awesome!"}

@app.get("/posts")
def get_posts():
    return {"msg": "This is the post you queried."}
