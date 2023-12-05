from pydantic import BaseModel, validator
from typing import List


class Child(BaseModel):
    name: str
    last_name: str
    age: int


class Person(BaseModel):
    name: str
    age: int
    childs: List[Child]


    @validator('name')
    def validate_name(cls, raw_name):  # кастомный валидатор имени
        min_len = 2
        max_len = 15
        if min_len <= len(raw_name) <= max_len:
            return raw_name
        else:
            raise ValueError(f"Name length must be in range [{min_len}, {max_len}] but actual length of {raw_name} = {len(raw_name)}")

    @validator('age')
    def validate_age(cls, raw_age):  # кастомный валидатор возраста
        min_age = 0
        max_age = 130
        if min_age <= raw_age <= max_age:
            return raw_age
        else:
            raise ValueError(f"Возраст должен быть в диаппазоне [{min_age}, {max_age}], указанный возраст = {raw_age}")