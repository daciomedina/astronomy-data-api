from abc import ABC, abstractmethod

from app.domain.stars.star import Star


class StarRepository(ABC):
    @abstractmethod
    def find_nearest(self, limit: int = 10) -> list[Star]:
        pass