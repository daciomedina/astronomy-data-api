from app.domain.stars.star import Star
from app.domain.stars.star_repository import StarRepository


class GetStarById:
    def __init__(self, repository: StarRepository) -> None:
        self.repository = repository

    def execute(self, star_id: str) -> Star | None:
        return self.repository.find_by_id(star_id)
