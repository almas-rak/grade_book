from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Score, Student
from ..schemas import ScoreCreate, ScoreUpdate
import logging

logger = logging.getLogger(__name__)


class ScoreRepository:
    @classmethod
    def get_score(cls, db: Session, score_id: int):
        score = db.query(Score).filter(Score.id == score_id).first()
        if not score:
            logger.error(f"Score with id {score_id} not found.")
        return score

    @classmethod
    def get_scores(cls, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Score).offset(skip).limit(limit).all()

    @classmethod
    def create_score(cls, db: Session, score: ScoreCreate):
        student = db.query(Student).filter(Student.id == score.student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail=f"Student with id {score.student_id} not found.")

        db_score = Score(score=score.score, student_id=score.student_id)
        try:
            db.add(db_score)
            db.commit()
            db.refresh(db_score)
            logger.info(
                f"Created score with id {db_score.id}, score: {db_score.score}, student: {student.name}, student_id: {student.id}"
            )
            return db_score
        except Exception as e:
            db.rollback()
            logger.error(f"Error creating score: {e}")
            raise HTTPException(status_code=500, detail=f"Error creating score: {e}")

    @classmethod
    def update_score(cls, db: Session, score_id: int, score_update: ScoreUpdate):
        db_score = db.query(Score).filter(Score.id == score_id).first()
        if db_score is None:
            raise HTTPException(status_code=404, detail=f"Score with id {score_id} not found.")

        try:
            if score_update.score is not None:
                db_score.score = score_update.score
            db.commit()
            db.refresh(db_score)
            logger.info(f"Updated score with id {db_score.id}.")
            return db_score
        except Exception as e:
            db.rollback()
            logger.error(f"Error updating score with id {score_id}: {e}")
            raise HTTPException(status_code=500, detail=f"Error updating score with id {score_id}: {e}")

    @classmethod
    def delete_score(cls, db: Session, score_id: int):
        db_score = db.query(Score).filter(Score.id == score_id).first()
        if db_score is None:
            logger.error(f"def delete_score:Score with id {score_id} not found.")
            raise HTTPException(status_code=404, detail=f"Score with id {score_id} not found.")
        try:
            db.delete(db_score)
            db.commit()
            logger.info(f"def delete_score: Deleted score with id {score_id}.")
        except Exception as e:
            db.rollback()
            logger.error(f"score_crud, def delete_score: Error deleting score with id {score_id}: {e}")
            raise
