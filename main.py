# DELETE Method
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
class UpdateStudent(BaseModel):
    name    : Optional[str] = None
    age     : Optional[int] = None
    email   : Optional[str] = None
    address : Optional[str] = None
    city    : Optional[str] = None
    state   : Optional[str] = None
    country : Optional[str] = None
    phone   : Optional[str] = None

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

@app.put('/update_students/{student_id}')
def create_students(student_id:int , student : UpdateStudent):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.email != None:
        students[student_id].email = student.email
    if student.address != None:
        students[student_id].address = student.address
    if student.city != None:
        students[student_id].city = student.city
    if student.state != None:
        students[student_id].state = student.state
    if student.country != None:
        students[student_id].country = student.country
    if student.phone != None:
        students[student_id].phone = student.phone

    return students[student_id]

@app.delete('/delete-student/{student_id}')
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"Student not found"}
    del students[student_id]
    return {"Success":"Successfully deleted"}
