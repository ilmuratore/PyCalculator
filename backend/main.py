from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Union
from backend.logic import add, subtract, multiply, divide

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Calculator API powered by Python FastAPI!"}

@app.get("/calculate")
def calculate (x:float, y:float, operation: str):
    if operation == "add":
        result = add(x, y)
    elif operation == "subtract":
        result = subtract(x, y)
    elif operation == "multiply":
        result = multiply(x, y)
    elif operation == "divide":
        result = divide(x, y)
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return JSONResponse(content={"result": result})

