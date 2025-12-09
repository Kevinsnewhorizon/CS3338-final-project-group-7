from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def amber():
    return {"amber": "MD Interface Running"}
