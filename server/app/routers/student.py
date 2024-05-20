from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Student


router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("/")
async def get_all_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()

    if students == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No student record found",
        )
    return students


@router.get("/{email}")
async def get_student_by_email(email: str, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.email == email).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"student with email: {email} not found",
        )
    return student
