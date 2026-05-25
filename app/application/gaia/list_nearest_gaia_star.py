from app.domain.gaia.gaia_star import GaiaStar
from app.domain.gaia.gaia_star_repository import GaiaStarRepository


class ListNearestGaiaStars:
    def __init__(self, repository: GaiaStarRepository) -> None:
        self.repository = repository

    def execute(self, limit: int = 10) -> list[GaiaStar]:
        return self.repository.find_nearest(limit=limit)