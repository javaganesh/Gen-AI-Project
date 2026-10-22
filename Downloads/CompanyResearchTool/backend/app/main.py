from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.reports import router as reports_router
from app.api.research import router as research_router

from app.database.models import Base
from app.database.connection import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Company Research Tool"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    health_router,
    prefix="/api"
)

app.include_router(
    reports_router,
    prefix="/api"
)

app.include_router(
    research_router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "message": "Company Research Tool Running"
    }