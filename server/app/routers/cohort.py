from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from ..models import Student
from ..database import get_db

router = APIRouter(prefix="/api/cohort", tags=["Cohort"])


@router.get("/stats/{cohort_name}")
async def get_cohort_stats(cohort_name: str, db: Session = Depends(get_db)):
    assignment_completion = func.avg(Student.assignment_completion).label(
        "avg_completion"
    )
    attendance_average = func.avg(Student.attendance_average).label("avg_attendance")

    # Subquery to count the distinct students
    total_students = (
        db.query(func.count(Student.id)).filter(Student.cohort == cohort_name).scalar()
    )
    print(total_students)

    cohort_stats = db.query(assignment_completion, attendance_average).first()
    # print(cohort_name, cohort_stats, total_students)

    if not cohort_stats:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cohort stats for '{cohort_name}' not found",
        )

    # avg_assignment_completion, avg_ranking, total_students = cohort_stats
    avg_assignment_completion, attendance_average = cohort_stats
    return {
        "assignment_completion": avg_assignment_completion,
        "attendance_average": attendance_average,
        "total_students": total_students,
    }


@router.get("/attendance/{cohort_name}")
async def get_cohort_attendance_stat(cohort_name: str, db: Session = Depends(get_db)):

    cohort_attendance_tuple = db.query(Student.attendance_average).all()
    cohort_attendance = [float(attendance[0]) for attendance in cohort_attendance_tuple]

    if not cohort_attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cohort attendance for '{cohort_name}' not found",
        )

    return cohort_attendance
