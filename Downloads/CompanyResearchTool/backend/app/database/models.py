from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Report(Base):

    __tablename__ = "reports"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    company_name = Column(
        String,
        nullable=False
    )

    overview = Column(Text)

    key_people = Column(Text)

    news = Column(Text)

    financials = Column(Text)

    risks = Column(Text)

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )