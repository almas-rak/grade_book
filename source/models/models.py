from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()


student = Table(
    "student",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

score = Table(
    "score",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("score", Integer, nullable=False),
    Column("student_id", Integer, ForeignKey(student.c.id))
)
