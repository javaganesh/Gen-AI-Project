import json
import asyncio

from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

from app.services.research_agent import research_company
from app.services.report_service import save_report

router = APIRouter()


@router.get("/research")
async def start_research(company_name: str):

    async def event_generator():

        try:

            yield {
                "event": "status",
                "data": "Research Started"
            }

            await asyncio.sleep(1)

            report = research_company(
                company_name
            )

            yield {
                "event": "overview",
                "data": report["overview"]
            }

            await asyncio.sleep(1)

            yield {
                "event": "key_people",
                "data": json.dumps(
                    report["key_people"]
                )
            }

            await asyncio.sleep(1)

            yield {
                "event": "news",
                "data": json.dumps(
                    report["news"]
                )
            }

            await asyncio.sleep(1)

            yield {
                "event": "financials",
                "data": json.dumps(
                    report["financials"]
                )
            }

            await asyncio.sleep(1)

            yield {
                "event": "risks",
                "data": json.dumps(
                    report["risks"]
                )
            }

            save_report(
                company_name,
                report
            )

            yield {
                "event": "complete",
                "data": "Research Finished"
            }

        except Exception as e:

            yield {
                "event": "error",
                "data": str(e)
            }

    return EventSourceResponse(
        event_generator()
    )