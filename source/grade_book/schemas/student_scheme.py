from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional


class StudentBase(BaseModel):
    name: constr(max_length=50)


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: Optional[constr(max_length=50)] = None


class Student(StudentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
