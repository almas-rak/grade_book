from fastapi import FastAPI
from grade_book.router import student_router, score_router
import logging
from logging_config import LOGGING

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Grade book"
)

app.include_router(student_router)
app.include_router(score_router)
