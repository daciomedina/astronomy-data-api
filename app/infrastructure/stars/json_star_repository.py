import json
from pathlib import Path

from app.domain.stars.star import Star
from app.domain.stars.star_repository import StarRepository


class JsonStarRepository(StarRepository):
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def find_nearest(self, limit: int = 10) -> list[Star]:
        stars = self._load_stars()

        return sorted(
            stars,
            key=lambda star: star.distance_light_years,
        )[:limit]

    def _load_stars(self) -> list[Star]:
        with self.file_path.open("r", encoding="utf-8") as file:
            raw_stars = json.load(file)

        return [Star(**star) for star in raw_stars]