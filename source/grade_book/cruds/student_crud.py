from sqlalchemy.orm import Session
from ..models import Student
from ..schemas import StudentCreate, StudentUpdate
import logging

logger = logging.getLogger(__name__)


class StudentRepository:
    @classmethod
    def get_student(cls, db: Session, student_id: int):
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            logger.error(f"Student with id {student_id} not found.")
        return student

    @classmethod
    def get_students(cls, db: Session, skip: int = 0, limit: int = 10):
        students = db.query(Student).offset(skip).limit(limit).all()
        return students

    @classmethod
    def create_student(cls, db: Session, student: StudentCreate):
        db_student = Student(name=student.name)
        try:
            db.add(db_student)
            db.commit()
            db.refresh(db_student)
            logger.info(f"Created student with id {db_student.id}.")
            return db_student
        except Exception as e:
            db.rollback()
            logger.error(f"Error creating student: {e}")
            raise

    @classmethod
    def update_student(cls, db: Session, student_id: int, student: StudentUpdate):
        db_student = db.query(Student).filter(Student.id == student_id).first()
        if db_student is None:
            logger.error(f"Student with id {student_id} not found.")
            return None
        try:
            db_student.name = student.name
            db.commit()
            db.refresh(db_student)
            logger.info(f"Updated student with id {db_student.id}.")
            return db_student
        except Exception as e:
            db.rollback()
            logger.error(f"Error updating student with id {student_id}: {e}")
            raise

    @classmethod
    def delete_student(cls, db: Session, student_id: int):
        db_student = db.query(Student).filter(Student.id == student_id).first()
        if db_student is None:
            logger.error(f"Student with id {student_id} not found.")
            return None
        try:
            db.delete(db_student)
            db.commit()
            logger.info(f"Deleted student with id {student_id}.")
        except Exception as e:
            db.rollback()
            logger.error(f"Error deleting student with id {student_id}: {e}")
            raise
