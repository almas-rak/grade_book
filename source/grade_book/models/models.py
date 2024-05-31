from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    scores = relationship("Score", back_populates="student")


class Score(Base):
    __tablename__ = "score"
    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'), index=True, name="student_id")
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    student = relationship("Student", back_populates="scores")

