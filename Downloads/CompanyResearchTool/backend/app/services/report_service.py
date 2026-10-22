import json

from app.database.connection import SessionLocal
from app.database.models import Report


def save_report(company_name, report_json):

    db = SessionLocal()

    report = Report(
        company_name=company_name,
        overview=report_json.get("overview", ""),
        key_people=json.dumps(
            report_json.get("key_people", [])
        ),
        news=json.dumps(
            report_json.get("news", [])
        ),
        financials=json.dumps(
            report_json.get("financials", {})
        ),
        risks=json.dumps(
            report_json.get("risks", [])
        )
    )

    db.add(report)

    db.commit()

    db.refresh(report)

    db.close()

    return report