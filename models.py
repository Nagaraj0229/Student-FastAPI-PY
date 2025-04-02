from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str
    age: int
    course: str
    city: Optional[str] = None
