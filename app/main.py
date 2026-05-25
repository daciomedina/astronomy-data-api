from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.v1.stars import router as stars_router
from app.api.v1.gaia import router as gaia_router

app = FastAPI(
    title="Astronomy Data API",
    description="Educational astronomy API built with FastAPI.",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(stars_router)
app.include_router(gaia_router)
