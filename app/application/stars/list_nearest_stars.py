from app.domain.stars.star import Star
from app.domain.stars.star_repository import StarRepository


class ListNearestStars:
    def __init__(self, repository: StarRepository) -> None:
        self.repository = repository

    def execute(self, limit: int = 10) -> list[Star]:
        return self.repository.find_nearest(limit=limit)