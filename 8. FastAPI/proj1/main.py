from fastapi import FastAPI, Query
from schemas import Person
from typing import List

app = FastAPI()


@app.get("/test1")
def read_item(parameter: List[str] = Query(["default1", "default2"], min_length=2, max_length=10)):  # валидация параметров??????
    return parameter


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/{key}")
def read_item(key: int):
    return {"key": key}


# @app.get("/{key}")
# def read_item(key: int, value1: int, value2: int):
#     print(key)
#     return {
#         "value1": value1,
#         "value2": value2,
#         "result": value1+value2
#     }


@app.post("/person")
def read_root(person: Person):
    return person
