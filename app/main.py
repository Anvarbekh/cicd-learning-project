
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CI/CD learning on a feature branch!"}
