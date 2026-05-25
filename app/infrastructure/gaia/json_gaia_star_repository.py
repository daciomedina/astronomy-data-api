import json
from pathlib import Path

from app.domain.gaia.gaia_star import GaiaStar
from app.domain.gaia.gaia_star_repository import GaiaStarRepository


class JsonGaiaStarRepository(GaiaStarRepository):
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def find_nearest(self, limit: int = 10) -> list[GaiaStar]:
        stars = self._load_stars()

        return sorted(
            stars,
            key=lambda star: star.distance_light_years,
        )[:limit]

    def _load_stars(self) -> list[GaiaStar]:
        with self.file_path.open("r", encoding="utf-8") as file:
            raw_stars = json.load(file)

        return [GaiaStar(**star) for star in raw_stars]