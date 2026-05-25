from pathlib import Path

from fastapi import APIRouter, HTTPException, Query, status

from app.api.schemas.star import StarResponse
from app.application.stars.get_star_by_id import GetStarById
from app.application.stars.list_nearest_stars import ListNearestStars
from app.infrastructure.stars.json_star_repository import JsonStarRepository

router = APIRouter(
    prefix="/api/v1/stars",
    tags=["Stars"],
)


def get_repository() -> JsonStarRepository:
    return JsonStarRepository(Path("data/stars.json"))


@router.get(
    "/nearest",
    response_model=list[StarResponse],
)
async def list_nearest_stars(
    limit: int = Query(default=10, ge=1, le=50),
) -> list[StarResponse]:
    repository = get_repository()
    use_case = ListNearestStars(repository)

    stars = use_case.execute(limit=limit)

    return [StarResponse.model_validate(star, from_attributes=True) for star in stars]


@router.get(
    "/{star_id}",
    response_model=StarResponse,
)
async def get_star_by_id(star_id: str) -> StarResponse:
    repository = get_repository()
    use_case = GetStarById(repository)

    star = use_case.execute(star_id)

    if star is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Star with id '{star_id}' was not found.",
        )

    return StarResponse.model_validate(star, from_attributes=True)
