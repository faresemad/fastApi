# path parameters
from fastapi import FastAPI , Path
app = FastAPI()
students = {
    1 : {
        "name": "Fares",
        "age": "21",
        "email": "fares@example.com",
        "address": "example",
        "city": "San Francisco",
        "state": "CA",
        "country": "US",
        "phone": "123-456-7890",
    },
    2 : {
        "name": "Shaimaa",
        "age": "20",
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

# @app.get('/students/{student_id}')
# def get_student(student_id:int):
#     return students[student_id]

@app.get('/students/{student_id}')
def get_student(student_id:int = Path(None,description="The ID of the student you want to view",gt=0,lt=3)):
    return students[student_id]
