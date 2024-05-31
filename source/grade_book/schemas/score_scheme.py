from pydantic import BaseModel, conint, constr
from typing import Optional
from datetime import datetime


class ScoreBase(BaseModel):
    score: conint(ge=1, le=12)


class ScoreCreate(ScoreBase):
    student_id: int


class ScoreUpdate(BaseModel):
    score: Optional[conint(ge=1, le=12)] = None


class Score(ScoreBase):
    id: int
    student_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
