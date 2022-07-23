# Request Body And The POST Method
from typing import Counter, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = {
    1 : {
        "name": "Fares",
        "age": 21,
        "email": "fares@example.com",
        "address": "example",
        "city": "San Francisco",
        "state": "CA",
        "country": "US",
        "phone": "123-456-7890",
    },
    2 : {
        "name": "Shaimaa",
        "age": 20,
        "email": "shaimaa@example.com",
        "address": "example",
        "city": "San Francisco",
        "state": "CA",
        "country": "US",
        "phone": "123-456-7890",
    }
}

class Student(BaseModel):
    name    : str
    age     : int
    email   : str
    address : str
    city    : str
    state   : str
    country : str
    phone   : str

@app.get('/')
def root():
    return {"Name" : "Fares Emad"}

@app.get('/get-std')
def get_std(name :Optional[str] = None , age :Optional[int] = None):
    for student_id in students:
        if (students[student_id]["name"] == name) or (students[student_id]["age"] == age):
            return students[student_id]
    return {"Msg" : "Not Found"}

@app.post('/create_students/{student_id}')
def create_students(student_id:int , student : Student):
    if student_id in students:
        return {"Error":"Student already exists"}
    students[student_id] = student
    return students[student_id]
