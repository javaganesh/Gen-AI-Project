from fastapi import APIRouter
from fastapi import HTTPException

from app.database.connection import SessionLocal
from app.database.models import Report

router = APIRouter()



@router.get("/reports")
def get_reports():

    db = SessionLocal()

    reports = (
        db.query(Report)
        .order_by(
            Report.generated_at.desc()
        )
        .all()
    )

    db.close()

    return reports


@router.get("/reports/{report_id}")
def get_report(report_id: int):

    db = SessionLocal()

    report = (
        db.query(Report)
        .filter(
            Report.id == report_id
        )
        .first()
    )

    db.close()

    if not report:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return report


@router.delete("/reports/{report_id}")
def delete_report(report_id: int):

    db = SessionLocal()

    report = (
        db.query(Report)
        .filter(
            Report.id == report_id
        )
        .first()
    )

    if not report:
        db.close()

        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    db.delete(report)

    db.commit()

    db.close()

    return {
        "message": "Report deleted"
    }