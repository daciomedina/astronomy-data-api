from pathlib import Path

from fastapi import APIRouter, Query

from app.application.stars.list_nearest_stars import ListNearestStars
from app.infrastructure.stars.json_star_repository import JsonStarRepository

router = APIRouter(
    prefix="/api/v1/stars",
    tags=["Stars"],
)


@router.get("/nearest")
async def list_nearest_stars(
    limit: int = Query(default=10, ge=1, le=50),
) -> list[dict[str, str | float]]:
    repository = JsonStarRepository(Path("data/stars.json"))
    use_case = ListNearestStars(repository)

    stars = use_case.execute(limit=limit)

    return [
        {
            "id": star.id,
            "name": star.name,
            "distance_light_years": star.distance_light_years,
            "apparent_magnitude": star.apparent_magnitude,
            "spectral_type": star.spectral_type,
        }
        for star in stars
    ]