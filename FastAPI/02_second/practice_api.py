from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
def index():
  return {"HI": "My first self hosted API"}

students = {
  1:{
    "name": "John",
    "age": 20,
    "year": 'Year 12'
  }
}

@app.get('/get_student/{student_id}')
def get_student(student_id: int= Path(..., description= "The ID of student")):
  return students[student_id]

@app.get('/get-by-name')
def get_student(*, name:str):
  for student_id in students:
    if students[student_id]["name"]== name:
      return students[student_id]
  return {"Data": "Not Found"}
