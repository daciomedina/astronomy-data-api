from pathlib import Path

from fastapi import APIRouter, Query

from app.api.schemas.gaia_star import GaiaStarResponse
from app.application.gaia.list_nearest_gaia_star import (
    ListNearestGaiaStars,
)
from app.infrastructure.gaia.json_gaia_star_repository import (
    JsonGaiaStarRepository,
)

router = APIRouter(
    prefix="/api/v1/gaia",
    tags=["Gaia"],
)


def get_repository() -> JsonGaiaStarRepository:
    return JsonGaiaStarRepository(
        Path("data/gaia_nearby_stars.json"),
    )


@router.get(
    "/stars/nearest",
    response_model=list[GaiaStarResponse],
)
async def list_nearest_gaia_stars(
    limit: int = Query(default=10, ge=1, le=50),
) -> list[GaiaStarResponse]:
    repository = get_repository()

    use_case = ListNearestGaiaStars(repository)

    stars = use_case.execute(limit=limit)

    return [
        GaiaStarResponse.model_validate(
            star,
            from_attributes=True,
        )
        for star in stars
    ]