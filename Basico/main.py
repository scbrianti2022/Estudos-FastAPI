from typing import Optional
from fastapi import FastAPI
import uvicorn


app = FastAPI(title='FastAPI Básica',
              version='0.0.1')




@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, p: bool, q: Optional[str] = None):
    return {"item_id": item_id, "q": q, "p": p}

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True)