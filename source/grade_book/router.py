from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated, List

from .database import SessionLocal
from .cruds import StudentRepository, ScoreRepository
from .schemas import student_scheme, score_scheme


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


student_router = APIRouter(
    prefix="/students",
    tags=["Студенты"]
)


@student_router.post("", response_model=student_scheme.Student, name="Добавить студента")
def create_student(student: Annotated[student_scheme.StudentCreate, Depends()], db: Session = Depends(get_db)):
    return StudentRepository.create_student(db=db, student=student)


@student_router.get("", response_model=List[student_scheme.Student], name="Получить список студентов")
def read_scores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = StudentRepository.get_students(db=db, skip=skip, limit=limit)
    return students


@student_router.get("/{student_id}", response_model=student_scheme.Student, name="Получить информацию о студенте")
def get_student(student_id: int, db: Session = Depends(get_db)):
    db_student = StudentRepository.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail=f"Student with id {student_id} not found")
    return db_student


@student_router.patch("/{student_id}", response_model=student_scheme.Student, name="Изменить данные студента")
def update_student(student_id: int, student: Annotated[student_scheme.StudentCreate, Depends()],
                   db: Session = Depends(get_db)):
    return StudentRepository.update_student(db, student_id, student)


@student_router.delete("/{student_id}", name="Удалить студента")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    StudentRepository.delete_student(db, student_id)
    return {"message": "Student deleted"}


score_router = APIRouter(
    prefix="/score",
    tags=["Оценки"]
)


@score_router.post("", response_model=score_scheme.Score, name="Добавить оценку")
def create_score(score: Annotated[score_scheme.ScoreCreate, Depends()], db: Session = Depends(get_db)):
    return ScoreRepository.create_score(db=db, score=score)


@score_router.get("", response_model=List[score_scheme.Score], name="Получить список оценок")
def read_scores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    scores = ScoreRepository.get_scores(db=db, skip=skip, limit=limit)
    return scores


@score_router.get("/{score_id}", response_model=score_scheme.Score, name="Получить информацию об оценке")
def read_score(score_id: int, db: Session = Depends(get_db)):
    db_score = ScoreRepository.get_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score


@score_router.patch("/{score_id}", response_model=score_scheme.Score, name="Изменить оценку")
def update_score(score_id: int, score: score_scheme.ScoreCreate, db: Session = Depends(get_db)):
    return ScoreRepository.update_score(db, score_id, score)


@score_router.delete("/{score_id}", name="Удалить оценку")
def delete_score(score_id: int, db: Session = Depends(get_db)):
    ScoreRepository.delete_score(db, score_id)
    return {"message": "Score deleted"}
