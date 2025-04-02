from fastapi import APIRouter, HTTPException
from database import students_collection
from models import Student
from bson import ObjectId

router = APIRouter()

# Create Student
@router.post("/students/")
async def create_student(student: Student):
    student_dict = student.dict()
    result = await students_collection.insert_one(student_dict)
    return {"id": str(result.inserted_id)}

# Get All Students
@router.get("/students/")
async def get_students():
    students = await students_collection.find().to_list(100)
    return students

# Get Student by ID
@router.get("/students/{student_id}")
async def get_student(student_id: str):
    student = await students_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

# Update Student
@router.put("/students/{student_id}")
async def update_student(student_id: str, student: Student):
    updated_student = await students_collection.update_one(
        {"_id": ObjectId(student_id)}, {"$set": student.dict()}
    )
    if updated_student.modified_count == 1:
        return {"message": "Student updated successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

# Delete Student
@router.delete("/students/{student_id}")
async def delete_student(student_id: str):
    deleted_student = await students_collection.delete_one({"_id": ObjectId(student_id)})
    if deleted_student.deleted_count == 1:
        return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")
