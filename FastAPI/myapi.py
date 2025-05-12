from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 20,
        "class": 'Year 12'
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
