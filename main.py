# Query Parameters
from typing import Optional
from fastapi import FastAPI
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

@app.get('/')
def root():
    return {"Name" : "Fares Emad"}

@app.get('/get-std')
def get_std(name :Optional[str] = None , age :Optional[int] = None):
    for student_id in students:
        if (students[student_id]["name"] == name) or (students[student_id]["age"] == age):
            return students[student_id]
    return {"Msg" : "Not Found"}

# http://127.0.0.1:8000/get-std?name=Fares
# http://127.0.0.1:8000/get-std?age=21
# http://127.0.0.1:8000/get-std?name=Fares&age=21
