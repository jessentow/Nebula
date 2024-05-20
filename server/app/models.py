from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Boolean, TIMESTAMP, ForeignKey

from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    name = Column(String)
    attendance_average = Column(Float)
    assignment_completion = Column(Integer)
    ranking = Column(Integer)
    cohort = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
