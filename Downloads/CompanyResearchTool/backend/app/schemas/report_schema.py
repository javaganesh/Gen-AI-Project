from pydantic import BaseModel

from typing import List
from typing import Optional


class KeyPerson(BaseModel):

    name: str

    title: str


class Financials(BaseModel):

    revenue: Optional[str] = None

    employee_count: Optional[str] = None

    market_cap: Optional[str] = None

    yoy_growth: Optional[str] = None


class ReportResponse(BaseModel):

    overview: str

    key_people: List[KeyPerson]

    news: List[str]

    financials: Financials

    risks: List[str]