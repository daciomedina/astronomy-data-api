from abc import ABC, abstractmethod

from app.domain.gaia.gaia_star import GaiaStar


class GaiaStarRepository(ABC):
    @abstractmethod
    def find_nearest(self, limit: int = 10) -> list[GaiaStar]:
        pass