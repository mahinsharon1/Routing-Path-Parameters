from fastapi import FastAPI

app = FastAPI()

students = {
    1: {
        "name": "Mahin",
        "age": 23,
        "course": "B.Tech CSE"
    },
    2: {
        "name": "Rahul",
        "age": 22,
        "course": "B.Tech IT"
    },
    3: {
        "name": "Arun",
        "age": 24,
        "course": "B.Tech AI"
    }
}

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]