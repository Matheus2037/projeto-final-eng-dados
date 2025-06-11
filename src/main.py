from typing import Union
from fastapi import FastAPI

app = FastAPI()

# Essa é pra dar sorte
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Rota principal
@app.get("/products/data")
async def get_products_data():
    return {}