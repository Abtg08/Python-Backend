from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    year: str 

class Update_student(BaseModel):
    name: Optional[str]= None
    age: Optional[int]= None
    year: Optional[str]= None
    

students = {
    1: {
        "name": "John",
        "age": 20,
        "year": 'Year 12'
    },
    # 3: {                              this shows that the value being passed is a dictionary and is not case sensitive
    #     'name': 'Anya',
    #     'age': 19,
    #     'role': 'Hero'    
    # }
}

@app.get('/')
def index():
    return {"name": "First Data"}

@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0, lt=5)):
    return students[student_id]

@app.get('/get-by-name')
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

@app.post('/create-student/{student_id}') 
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student with this ID already exists"}
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: Update_student):
    if student_id not in students:
        return {"Error": "Student not found"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age!=None:
        students[student_id].age = student.age
    if student.year!=None:
        students[student_id].year = student.year
    return students[student_id]


@app.delete('/delete-student:{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student not found"}
    del students[student_id]
    return {"Message": "Student deleted successfully"}

